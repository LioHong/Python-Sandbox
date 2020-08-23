'''
Name: Mastermind00
Date: 20181218
Author: Lio Hong
Purpose: Create a hangul letter freq counter
Setup a dict for each composite syllable
relating to their component letters
Print each hangul syllable seqeuntially
in Unicode
'''
sample = '조선 세종(朝鮮 世宗, 1397년 5월 15일[1] (음력 4월 10일) ~ 1450년 3월 30일 (음력 2월 17일), 재위 1418년 ~ 1450년)은 조선의 제4대 군주이며 언어학자이다. 그의 업적에 대한 존경의 의미를 담은 명칭인 세종대왕(世宗大王)으로 자주 일컬어진다.'
sample2 ='성은 이(李), 휘는 도(祹), 본관은 전주(全州), 자는 원정(元正), 아명은 막동(莫同)이다. 세종은 묘호이며, 시호는영문예무인성명효대왕(英文睿武仁聖明孝大王)이고, 명나라에서 받은 시호는 장헌(莊憲)이다. 존시를 합치면 세종장헌영문예무인성명효대왕(世宗莊憲英文睿武仁聖明孝大王)이 된다. 태종과 원경왕후의 셋째 아들이며, 비는 청천부원군(靑川府院君) 심온의 딸 소헌왕후 심씨(昭憲王后 沈氏)이며, 조선의 왕 중에서 왕세자에게 양위를 하지 않고 훙서한 최초의 왕이다.[2][3]한성 준수방(지금의 서울특별시 종로구 통인동) 고을에서 아버지 정안군 이방원과 어머니 민씨 부인의 셋째 아들로 태어났으며 태종 8년(1408년) 충녕군(忠寧君)에 봉해졌다가, 태종 12년(1412년), 둘째 형 효령군 이보와 함께 대군으로 진봉된다. 1418년 첫째 형 양녕대군이 왕세자에서 폐위되면서 세자로 책봉되었고 얼마 후 부왕의 선위로 즉위하였다. 즉위 초반 4년간 부왕 태종이 대리청정을 하며 국정과 정무를 주관하였고 이때 장인 심온과 그의 측근들이 사형에 처해졌다. 이후 주변의 소헌왕후 폐출 주장을 일축했고, 건강이 좋지 않았던 그는 김종서, 맹사성 등을 등용하여 정무를 주관하였는데 이 통치체제는 일종의 내각 중심 정치제도인 의정부서사제의 효시가 되었다. 세종은 과학, 예술, 문화등 많은 분야에서 뛰어난 왕이었다. 그는 백성들에게 농사에 관한 책을 퍼내었지만 글을 읽지 못해 보지 못하는 모습을 보고[4] 1443년 누구나 쉽게 배울 수 있는 효율적이고 과학적인 문자 체계인 훈민정음(訓民正音)을 창제하였다. 이것은 20세기 주시경에 의해 한글로 발전되어, 오늘날 대한민국과 조선민주주의인민공화국을 비롯한 한반도에서 공식 문자로서 널리 쓰이고 있다. 10월 9일은 한글날로 기념한다. 과학 기술에도 두루 관심을 기울여혼천의, 앙부일구, 자격루, 측우기 등의 발명을 전폭적으로 지원했고, 신분을 뛰어넘어 장영실, 최해산 등의 학자들을 적극 후원하였다. 국방에 있어서는 이징옥, 최윤덕 등을 북방으로 보내 평안도와 함길도에 출몰하는 여진족을 국경 밖으로 몰아내고 4군 6진을 개척하여 압록강과 두만강 유역으로 국경을 확장하였고, 백성들을 옮겨 살게 하는 사민정책(徙民政策)을 실시하여 국토의 균형된 발전을 위해서도 노력하였다. 또한 이종무를 파견하여 왜구를 토벌하고대마도를 정벌하였다. 이밖에도 법전과 문물을 정비하였고 조세 제도의 확립에도 업적을 남겼다.'
def hangulFreq(text):
    import re
    import collections
    hgPure = re.sub(r'[^\uAAC0-\uD7A3]', '', text)
    print(hgPure)
    hgFreq = collections.Counter(hgPure)

    check = 0
    for i in hgFreq:
        check += hgFreq[i]

    #print(check)
    #print(len(hgPure))
    if check == len(hgPure):
        print('Counts match.')
    
    return hgFreq

def hangulDecomp(syllable):
    hgVal = ord(syllable)
    normVal = hgVal - 0xac00
    final = normVal % 28 + 0x11A7
    medial = (normVal//28) % 21 + 0x1161
    initial = (normVal//28) // 21 + 0x1100
    components = [initial, medial, final]
    components2 = [chr(i) for i in components]
    #components2[0] += ':'
    return components2
    
def jamoFreq(text):
    hgFreq = hangulFreq(text)
    jmFreq = {}
    print(hgFreq)
    print('Jamo frequencies')
    for key in hgFreq:
        jamoParts = hangulDecomp(key)
        for j in jamoParts:
            if j not in jmFreq:
                jmFreq[j] = hgFreq[key]
            else:
                jmFreq[j] += hgFreq[key]
    print(jmFreq)
    print(len(jmFreq))

jamoFreq(sample)
jamoFreq(sample2)