# 肺炎期间免费下载出版社提供的教材
疫情期间，应教育部要求，各个中小学教材出版社都将pdf电子版的下载链接放了出来，供大家免费下载。

[《关于发布中小学国家课程教材电子版链接的通告》](http://www.moe.gov.cn/jyb_xxgk/s5743/s5744/202002/t20200213_420774.html)

不过教材种类过于繁多，一个个点击下载太耗费时间，所以写了一个简单的脚步来实现一键下载



2020-02-17：只做了人教版的，其他出版社待补充



### 准备工作

1. 安装Python3

2. 下载脚本：

   - 如果没有Git，下载https://github.com/yangzm11/DownloadingTextbooksScripts/archive/master.zip，然后解压缩。用命令行进入解压的文件夹

   - 如果安装了Git，输入

     `git clone https://github.com/yangzm11/DownloadingTextbooksScripts.git`

     然后

     `cd DownloadingTextbooksScripts`



### 人教版

输入

`python DownloadTextbooks-pep.py`

等待大约40分钟（视网速），直到显示“全部下载完毕”。
