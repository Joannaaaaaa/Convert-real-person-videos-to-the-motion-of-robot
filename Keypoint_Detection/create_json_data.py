import json

ss='{"images": ['
for i in range(100):
    ss += '{"file_name": "'+str(i)+'.jpg","id": '+str(i)+'},\n'
ss += '{"file_name": "100.jpg","id": 100}]}'
    
print(ss)

ss = json.loads(ss)
with open('./data/plot_img/annotations/person_keypoints_val2017.json', 'w') as f:
    json.dump(ss, f, indent=2)