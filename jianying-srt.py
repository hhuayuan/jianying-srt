# coding = utf-8

import json
import argparse


def json_to_txt(json_file_name, txt_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as f:
        jsons = json.load(f)

    # print(jsons['materials']['texts'])
    # print(jsons['tracks'])
    with open(txt_file_name, 'w', encoding='utf-8') as f:
        for item in jsons['materials']['texts']:
            f.write('%s,%s\n' % (item['id'], item['content']))

    # for item in jsons['tracks']:
    #     segments = item['segments']
    # print(item['segments'])
    # for segment in segments:
    #     print(segment['material_id'])
    #     print(segment['target_timerange'])
    #     print(segment['target_timerange']['duration'])
    #     print(segment['target_timerange']['start'])


def txt_to_json(txt_file_name, json_file_name):
    srt_dict = {}
    with open(json_file_name, 'r', encoding='utf-8') as f:
        jsons = json.load(f)

    with open(txt_file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            a = line.strip('\n').split(',')
            srt_dict[a[0]] = a[1]

    for item in jsons['materials']['texts']:
        item['content'] = srt_dict[item['id']]
        print(item['content'])
        # print(item['id'], item['content'])

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(jsons, f, ensure_ascii=False)  # ensure_ascii=False 避免中文乱码


if __name__ == '__main__':
    json_file = 'draft_content.json'
    txt_file = 'temp.txt'
    parser = argparse.ArgumentParser(description='剪映字幕导出批量修改工具。')
    parser.add_argument('-j', '--json_file_name', type=str, help='剪映字幕文件的完整路径，默认在当前目录下生成查找draft_content.json文件。')
    parser.add_argument('-t', '--txt_file_name', type=str, help='导出的字幕文本文件完整路径，默认在当前目录下生成temp.txt文件。')
    parser.add_argument('-c', '--command', type=str.lower, choices=['tojson', 'totxt'],
                        help='转换类型，默认为把剪映字幕文件导出到文本文件(totxt)')
    args = parser.parse_args()
    if args.json_file_name:
        json_file = args.json_file_name
    if args.txt_file_name:
        txt_file = args.txt_file_name
    if args.command:
        command = args.command
    else:
        command = 'totxt'

    if command == 'totxt':
        json_to_txt(json_file_name=json_file, txt_file_name=txt_file)
    else:
        txt_to_json(txt_file_name=txt_file, json_file_name=json_file)
