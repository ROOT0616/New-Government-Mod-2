"""Regenerate menu events and ruler job definitions from the checked-in catalogs."""
import argparse, json, re
from pathlib import Path

def scalar(v):
    return v if v and re.fullmatch(r'[^\s{}#"=<>!]+',v) else json.dumps(v,ensure_ascii=False)
def render(tree, depth=0):
    out=[]
    for key, op, value in tree:
        lead=scalar(key)+' '+op+' ' if key is not None else ''
        if isinstance(value,list):
            out.extend(['\t'*depth+lead+'{',render(value,depth+1).rstrip(), '\t'*depth+'}'])
        else:
            out.append('\t'*depth+lead+(json.dumps(value,ensure_ascii=False) if key=='name' else scalar(value)))
    return '\n'.join(x for x in out if x)+'\n'

def generated(data):
    catalog=json.loads((data/'ruler-jobs.json').read_text(encoding='utf-8'))
    deposit='d_ngm_civic_ruler_jobs = {\n category = deposit_cat_rare icon = d_monument_in_space\n potential = { always = no } drop_weight = { weight = 0 }\n'
    values='ngm_civic_ruler_replacement_count = { base = 0\n'
    for r in catalog['rows']:
        gate=f'has_building = {r["building"]} exists = owner owner = {{ has_valid_civic = {r["civic"]} }}'
        deposit+=f' triggered_planet_modifier = {{ potential = {{ {gate} }} {r["job_modifier"]} = {r["amount"]} }}\n'
        values+=f' modifier = {{ {gate} add = {r["amount"]} }}\n'
    deposit+=' triggered_planet_modifier = { potential = { exists = owner owner = { is_gestalt = no is_worker_coop_empire = no } } job_politician_add = -1 mult = value:ngm_civic_ruler_replacement_count }\n}\n'
    for building,cap in catalog['capital_caps'].items():
        values+=f' if = {{ limit = {{ has_building = {building} }} max = {cap} }}\n'
    values+='}\n'
    menu=json.loads((data/'avantgarde-menu.json').read_text(encoding='utf-8'))
    return {'common/deposits/NGM_civic_ruler_jobs.txt':deposit,
            'common/script_values/NGM_civic_ruler_values.txt':values,
            'events/NGM_avantgarde_menu_generated.txt':'# Generated from tools/data/avantgarde-menu.json.\nnamespace = ngm_tradition\n'+render(menu)}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);args=ap.parse_args()
    for rel,text in generated(Path(__file__).parent/'data').items():
        (args.root/rel).write_text(text,encoding='utf-8',newline='\n')
    print('Generated 3 files from catalogs')
