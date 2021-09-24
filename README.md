## 剪映字幕文件导出文本文件批量编辑

简介
---

剪映PC版有自动识别字幕功能，但是识别会有一定的误差，需要根据实际情况对字幕进行修改。剪映软件只能选中需要修改的单条字幕文本进行修改，字幕内容多的时候效率比较低。为了提高字幕编辑效率就开发了这个脚本把剪映的字幕内容导出到文本文件，集中修改好后再导回去。

参数说明
---
python jianying-srt.py -j draft_content.json -t temp.txt -c totxt

### -j
选填，需要导出的剪映字幕文件完整路径，默认会在当前目录下查找draft_content.json文件。

### -t
选填，导出后的文本文件完整路径，默认会在当前目录下查找temp.txt文件。

### -c
选填，导入\导出选项，totxt是把剪映字幕json文件导出到文本文件，tojson是把编辑好的文本文件导入到剪映字幕json文件。

备注
---
剪映的字幕文件可以到它的安装目录找，以下是剪映默认的草稿路径：

C:\Users\(你的用户名)\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft

本脚本在剪映PC版V1.3.6下测试通过。

