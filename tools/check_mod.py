"""Portable structural checks. No game installation or third-party packages needed."""
from pathlib import Path
import argparse,collections,json,sys
import clausewitz_parser as cw

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args();root=args.root.resolve();errors=[];event_ids={};trees={};files=0
    for folder in ('common','events','interface'):
        for p in (root/folder).rglob('*'):
            if not p.is_file() or p.suffix not in ('.txt','.gui','.gfx'):continue
            rel=p.relative_to(root).as_posix();tree=cw.parse(p.read_text(encoding='utf-8-sig'),rel);trees[rel]=tree;files+=1
            if folder=='events':
                for k,o,v in tree:
                    if not isinstance(v,list):continue
                    id=cw.first(v,'id')
                    if not id:errors.append(f'{rel}: event without ID')
                    elif id in event_ids:errors.append(f'{id}: duplicate event ID')
                    else:event_ids[id]=rel
    errors.extend(cw.errors)
    for rel,tree in trees.items():
        if not rel.startswith('common/on_actions/'):continue
        for k,o,v in cw.walk(tree):
            if k=='events' and isinstance(v,list):
                for a,b,id in v:
                    if isinstance(id,str) and id.lower().startswith(('ngm_','gft_')) and id not in event_ids:errors.append(f'{rel}: unresolved event {id}')
    descriptor=cw.parse((root/'descriptor.mod').read_text(encoding='utf-8-sig'),'descriptor.mod')
    if cw.values(descriptor,'replace_path'):errors.append('Unexpected replace_path')
    if cw.values(descriptor,'remote_file_id'):errors.append('Development descriptor contains Workshop upload ID')
    bom_warnings=[]
    for p in (root/'localisation').rglob('*.yml'):
        if not p.read_bytes().startswith(b'\xef\xbb\xbf'):bom_warnings.append(p.relative_to(root).as_posix())
    result=dict(version=cw.first(descriptor,'version'),passed=not errors,script_files=files,event_ids=len(event_ids),errors=errors,localization_bom_warnings=bom_warnings,runtime_tested=False)
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['passed'] else 1

if __name__=='__main__':sys.exit(main())
