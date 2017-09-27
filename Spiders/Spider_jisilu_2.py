#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-27 9:02:49
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/


import ssl
from selenium import webdriver

# 取消证书认证
ssl._create_default_https_context = ssl._create_unverified_context()
# 调用PhantomJS启动浏览器
browser = webdriver.PhantomJS()
# 打开链接
browser.get('https://www.jisilu.cn/data/cbnew/#tlink_3')
# 延迟3秒，等待页面加载完成
browser.implicitly_wait(3)
# 打开文件并以追加模式写入
with open('kzz.txt', 'a') as fp:
    a = 0
    # 匹配前四行数据，并循环处理
    for tr in browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr'):
        # # 获取每行的前面11条数据
        # for i in range(11):
        a += 1
        if a % 2 == 0:
            for i in range(23):
                # 以空格分割每行数据，并迭代获取数据
                content = tr.text.split(' ')[i]
                # content 为 tuple 类型，用小标提取后进行硬编码为utf-8
                fp.write(content.encode('utf-8'))
                fp.write('\t')
            # 写入一行数据后换行
            fp.write('\n')

## kzz.txt
# 113009	广汽转债	127.00	0.00%	广汽集团	27.21	0.00%	3.73	21.430	126.97	0.02%	购买	购买	15.00	27.86	1.8%	22-01-22	4.323	-3.23%	-3.65%	购买	0.00	0.84
# 128014	永东转债	117.00	0.00%	永东股份	22.82	0.00%	4.02	20.460	111.53	4.90%	购买	购买	14.32	26.60	10.1%	23-04-17	5.556	-0.56%	-0.99%	购买	0.00	0.00
# 132009	17中油EB	101.69	0.00%	中国石油	8.09	0.00%	1.17	8.920	90.70	12.36%	购买	购买	6.24	11.60	0.7%	22-07-13	4.795	1.44%	1.08%	购买	0.00	0.67
# 113011	光大转债	110.70	0.00%	光大银行	4.10	0.00%	0.81	4.260	96.24	15.02%	购买	购买	-	5.54	15.7%	23-03-17	5.471	-0.12%	-0.46%	购买	0.00	0.74
# 113013	国君转债	124.28	0.00%	国泰君安	21.71	0.00%	1.45	20.200	107.48	15.64%	购买	购买	-	26.26	3.7%	23-07-06	5.775	-2.13%	-2.43%	购买	0.00	0.83
# 132012	17巨化EBQ	100.95	0.00%	巨化股份	11.57	0.00%	2.32	13.600	85.07	18.74%	购买	购买	9.52	17.68	8.2%	20-09-04	2.940	1.34%	1.00%	购买	0.00	0.00
# 128015	久其转债	112.20	0.00%	久其软件	12.12	0.00%	4.16	12.900	93.95	19.42%	购买	购买	9.03	16.77	9.1%	23-06-08	5.699	0.06%	-0.34%	购买	0.00	0.00
# 132010	17桐昆EBQ	114.00	0.00%	桐昆股份	16.19	0.00%	1.36	17.120	94.57	20.71%	购买	购买	11.98	20.54	5.0%	20-08-03	2.852	-2.92%	-3.24%	购买	0.00	0.00
# 127004	模塑转债	107.10	0.00%	模塑科技	6.93	0.00%	1.70	8.000	86.62	23.64%	购买	购买	5.60	10.40	0.0%	23-06-02	5.682	1.37%	0.87%	购买	0.00	0.00
# 132011	17浙报EBQ	92.70	0.00%	浙数文化	17.40	0.00%	3.17	25.000	69.60	33.35%	购买	购买	17.50	32.50	10.6%	22-08-17	4.890	3.01%	2.72%	购买	0.00	0.62
# 123001	蓝标转债	105.22	0.00%	蓝色光标	7.44	0.00%	2.34	9.770	76.15	38.17%	购买	购买	6.84	12.70	8.8%	21-12-18	4.227	1.74%	1.17%	购买	0.00	0.33
# 127003	海印转债	101.48	0.00%	海印股份	3.72	0.00%	2.69	5.250	70.86	43.22%	购买	购买	3.67	6.83	13.3%	22-06-08	4.699	2.75%	2.16%	购买	0.00	0.00
# 128012	辉丰转债	102.83	0.00%	辉丰股份	5.37	0.00%	2.02	7.740	69.38	48.21%	购买	购买	5.42	10.06	10.4%	22-04-21	4.567	0.96%	0.64%	购买	0.00	0.00
# 132008	17山高EB	95.22	0.00%	山东高速	5.94	0.00%	1.17	9.800	60.61	58.30%	购买	购买	6.86	12.74	8.7%	22-04-24	4.575	4.08%	3.46%	购买	0.00	0.64
# 132004	15国盛EB	92.25	0.00%	上海建工	3.87	0.00%	1.31	6.760	57.25	62.70%	购买	购买	4.73	8.79	17.3%	21-11-05	4.110	3.76%	3.35%	购买	0.00	0.62
# 132002	15天集EB	103.50	0.00%	天士力	35.13	0.00%	5.56	56.020	62.71	65.54%	购买	购买	44.82	75.63	3.2%	20-06-08	2.699	-0.29%	-0.51%	购买	0.00	0.47