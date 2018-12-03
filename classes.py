"""
classes = ['粒细胞系统-嗜碱性-晚幼粒细胞', '浆细胞系统-浆细胞', '粒细胞系统-嗜中性-中幼粒细胞',
           '成熟红细胞', '巨核细胞系统-颗粒性巨核细胞', '粒细胞系统-嗜中性-晚幼粒细胞',
           '粒细胞系统-嗜酸性-分叶核', '单核细胞系统-单核细胞', '红细胞系统-原红细胞',
           '粒细胞系统-嗜酸性-晚幼粒细胞', '红细胞系统-早幼红细胞', '粒细胞系统-嗜中性-分叶核',
           '粒细胞系统-嗜酸性-中幼粒细胞', '粒细胞系统-早幼粒细胞', '红细胞系统-中幼红细胞',
           '原始细胞', '血小板', '粒细胞系统-嗜碱性-中幼粒细胞', '单核细胞系统-幼单核细胞',
           '淋巴细胞系统-小淋巴细胞', '其他细胞-退化细胞', '粒细胞系统-嗜中性-带形核',
           '淋巴细胞系统-大淋巴细胞', '红细胞系统-晚幼红细胞', '巨核细胞系统-产生血小板性巨核细胞']
"""

classes = ['其他细胞-退化细胞','单核细胞系统-单核细胞','单核细胞系统-幼单核细胞','原始细胞',
			'巨核细胞系统-产生血小板性巨核细胞','巨核细胞系统-颗粒性巨核细胞',
			'成熟红细胞','浆细胞系统-浆细胞','淋巴细胞系统-大淋巴细胞',
			'淋巴细胞系统-小淋巴细胞','粒细胞系统-嗜中性-中幼粒细胞',
			'粒细胞系统-嗜中性-分叶核','粒细胞系统-嗜中性-带形核',
			'粒细胞系统-嗜中性-晚幼粒细胞','粒细胞系统-嗜碱性-中幼粒细胞',
			'粒细胞系统-嗜碱性-晚幼粒细胞','粒细胞系统-嗜酸性-中幼粒细胞',
			'粒细胞系统-嗜酸性-分叶核','粒细胞系统-嗜酸性-晚幼粒细胞',
			'粒细胞系统-早幼粒细胞','红细胞系统-中幼红细胞',
			'红细胞系统-原红细胞','红细胞系统-早幼红细胞',
			'红细胞系统-晚幼红细胞','血小板']
			
			


if __name__ == '__main__':
    with open('synset.txt','w') as f:
        for i in range(len(classes)):
            f.write(str(i) + ' ' + classes[i] + '\n')