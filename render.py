from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import hashlib

W = H = 1024
PAPER = '#F7F2E7'; INK = '#111111'; NAVY = '#102A4A'; RED = '#A41E22'; GREY = '#655F55'; RULE = '#B9B1A4'
im = Image.new('RGB', (W,H), PAPER); d = ImageDraw.Draw(im)
base = Path(__file__).parent
fontdir = Path('/usr/share/fonts/truetype/dejavu')
def font(file, size): return ImageFont.truetype(str(fontdir/file), size)
serif = lambda s: font('DejaVuSerif-Bold.ttf',s)
sans = lambda s: font('DejaVuSans.ttf',s)
bold = lambda s: font('DejaVuSans-Bold.ttf',s)
def wrapped(text, f, width):
    out=[]
    for para in text.split('\n'):
        line=''
        for word in para.split():
            test=(line+' '+word).strip()
            if d.textbbox((0,0),test,font=f)[2] <= width: line=test
            else:
                if not line: raise ValueError('word exceeds box: '+word)
                out.append(line); line=word
        out.append(line)
    return out
def textbox(text, x,y,w,h,f, fill=INK, maxlines=None, leading=None):
    lines=wrapped(text,f,w); lead=leading or f.size+2
    if maxlines is not None and len(lines)>maxlines: raise ValueError(f'text overflow ({len(lines)}>{maxlines}): {text}')
    if len(lines)*lead > h: raise ValueError('text exceeds box height: '+text)
    for i,line in enumerate(lines): d.text((x,y+i*lead),line,font=f,fill=fill)
    return len(lines)
def rule(y,x1=18,x2=1006,color=INK): d.line((x1,y,x2,y),fill=color,width=1)

# Masthead
d.text((20,8),'THE WORLD TODAY',font=serif(37),fill=INK)
d.text((692,12),'TUESDAY, 24 NOVEMBER 2026',font=bold(15),fill=INK)
d.text((790,36),'THE DAY IN ONE PAGE',font=bold(13),fill=GREY)
d.text((20,54),'36 STORIES  -  9 REGIONS  -  ALL DATED  -  24 NOVEMBER 2026',font=bold(14),fill=RED)
rule(76)

# Lead text and schematic map
d.text((20,84),'UKRAINE  /  LIBYA  /  WAR AT SEA',font=bold(13),fill=RED)
textbox('UKRAINE SEA DRONES SINK RUSSIAN WARSHIP OFF LIBYA',20,104,590,60,serif(23),maxlines=2,leading=29)
textbox('Monday Zelensky confirmed seven Ukrainian sea drones sank the 2023-commissioned Russian corvette Merkury at Benghazi (attack, Sun 23 Nov). A Ka-27 was destroyed; cargo ship MV Angara was hit.',20,166,585,62,sans(12),maxlines=3,leading=16)
# map box
d.rectangle((626,83,1004,231),fill='#DCE8E8',outline=RULE,width=1)
d.polygon([(626,83),(742,83),(725,115),(700,129),(682,155),(654,151),(626,168)],fill='#D9CCAE',outline=GREY)
d.polygon([(805,83),(1004,83),(1004,231),(946,221),(923,196),(892,181),(861,151),(835,145)],fill='#D9CCAE',outline=GREY)
d.polygon([(626,210),(698,204),(746,219),(805,208),(852,222),(911,216),(1004,223),(1004,231),(626,231)],fill='#D9CCAE',outline=GREY)
d.text((844,189),'LIBYA',font=bold(10),fill=INK); d.ellipse((854,179,862,187),fill=RED); d.text((865,175),'BENGHAZI',font=bold(9),fill=RED)
for pts in [((665,126),(755,145),(842,178)),((691,139),(779,159),(848,181)),((720,123),(796,151),(852,181))]:
    d.line(pts,fill=RED,width=2)
d.polygon([(846,168),(851,179),(863,175),(855,184),(861,194),(850,188),(842,196),(845,184),(836,179)],fill=RED)
d.polygon([(777,158),(805,153),(818,158),(804,162),(780,162)],fill=NAVY); d.text((774,145),'MERKURY',font=bold(9),fill=NAVY)
d.text((756,174),'Ka-27',font=bold(9),fill=INK)
d.text((634,218),'SCHEMATIC  -  BENGHAZI, LIBYA',font=bold(9),fill=INK)
d.rectangle((18,234,1006,257),fill=NAVY)
d.text((29,237),'7 DRONES  -  1 CORVETTE SUNK  -  1 Ka-27 DESTROYED  -  1 CARGO SHIP HIT',font=bold(14),fill='white')

# Hormuz strip
d.text((20,262),'MIDDLE EAST  /  WAR AT SEA',font=bold(12),fill=RED)
textbox('THREE TANKERS ABLAZE AFTER HITTING MINES IN HORMUZ',20,278,785,25,serif(19),maxlines=1,leading=22)
textbox("Iran's Revolutionary Guards say three tankers caught fire after striking mines east of the Strait on Mon and Tue; a fourth tanker was also hit. The US is probing Iranian links to cyberattacks on up to 50 vessels; oil jumped.",20,303,790,39,sans(11),maxlines=2,leading=14)
for sx in (835,890,945):
    d.polygon([(sx,302),(sx+39,302),(sx+33,313),(sx+5,313)],fill=NAVY); d.rectangle((sx+13,295,sx+25,302),fill=NAVY); d.line((sx+20,293,sx+17,286),fill=RED,width=2); d.line((sx+20,293,sx+24,285),fill=RED,width=2)
rule(346)

# 12-panel grid: literal story data (region, headline, fact deck).
PANELS=[
('CLIMATE','COP31 COLLAPSES IN ANTALYA','50 overtime hours; 90+ nations and EU reject draft omitting fossil fuels.'),
('CHINA','SHANGHAI CHIEF CHEN JINING PROBED','Politburo member probed over discipline and laws; fourth top leader since 2025.'),
('MARKETS','DOW TOPS 50,000 FIRST TIME','Dow closes above 50,000; Nasdaq slips as Nvidia gives back Monday gains.'),
('EUROPE','RUSSIAN STRIKE HITS ZAPORIZHZHIA','Russian attack kills 2, injures 40, after the ship attack off Libya.'),
('ASIA','HASINA PLANS 16 DEC RETURN','Exiled PM plans return from India. Garment workers win 36% pay rise.'),
('EUROPE','SARKOZY TO STAND TRIAL IN 2027','Former president faces corruption trial from 1 Apr 2027.'),
('ASIA','INDONESIA FACTORY FIRE TOLL 26','Rescuers: most died trying to reach the emergency exit.'),
('MIDDLE EAST','ISRAELI STRIKE KILLS HAMAS CHIEF','Gaza toll since truce: 1,690. Hamas agreed to disarm, Board of Peace says.'),
('COURTS','HUAWEI CONVICTED IN US TRIAL','Iran bank fraud, sanctions convictions; acquitted of racketeering, obstruction.'),
('BUSINESS','SANOFI BUYS INSMED FOR 41BN','$41bn cash, $175/share; biggest pharma deal since 2023. Close H1 2027.'),
('SECURITY','NATO COUNTS 25 AIRSPACE VIOLATIONS','25 Russian violations in 2026; 20 Nov debris found in Poland.'),
('SPACE','TIANGONG WELCOMES ASTRONAUT','Pakistani Zeeshan Ali arrives on Shenzhou-24: first foreign astronaut.')]
for i,(region,headline,deck) in enumerate(PANELS):
    x=20+(i%4)*247; y=351+(i//4)*121
    if i%4: d.line((x-8,y-4,x-8,y+117),fill=RULE)
    # Distinct miniature symbols: globe, person, chart, blast, arrow,
    # scales, factory, target, courthouse, pill, shield and satellite.
    symbols=['◎','♟','↗','✦','➜','⚖','▥','⊕','▤','✚','◇','✧']
    d.text((x+212,y),symbols[i],font=sans(21),fill=NAVY)
    textbox(region+' / 24 NOV',x,y,210,14,bold(10),RED,maxlines=1)
    textbox(headline,x,y+26,233,38,serif(15),maxlines=2,leading=18)
    textbox(deck,x,y+67,233,44,sans(11),maxlines=3,leading=14)
    if i%4==3: rule(y+117,color=RULE)
textbox('TECHNOLOGY / COURTS / 24 NOV',20,717,984,16,bold(11),RED,maxlines=1)
textbox('STATES SUE SPACEX OVER GROK ABUSE IMAGES',20,735,984,25,serif(20),maxlines=2,leading=23)
textbox('Oregon and Virginia sued SpaceX Super Intelligence on Monday 23 Nov, alleging Grok generated sexual images of children: the first such state suits. A cited CCDH study estimated 3 million sexualised X images (29 Dec 2025–8 Jan 2026), about 23,000 appearing to depict children.',20,763,984,42,sans(11),maxlines=3,leading=14)
rule(809)
textbox('ALSO TODAY',20,814,190,24,serif(18),maxlines=1)
textbox('TWENTY-ONE MORE DEVELOPMENTS, ALL DATED / 24 NOV',210,819,790,16,bold(11),RED,maxlines=1)
# Also Today: literal brief data (number, region tag, one-line brief).
BRIEFS=[
('01','MARKETS','Huang back as NVIDIA CEO; Nasdaq up 6.51 %'),
('02','WAR AT SEA','Sparta II burns in Baltic; 16 crew evacuated'),
('03','DIPLOMACY','No Ukraine deal at Shenzhen, 19 Nov'),
('04','JUSTICE','14 states back Rohingya case at the ICJ'),
('05','MIDDLE EAST','US sanctions Iran; Qatar mediates talks'),
('06','DISASTER','Nepal shaken by a 5.6 quake by China border'),
('07','HEALTH','Measles ninth death in Pennsylvania'),
('08','AMERICAS','Car bomb in Villavicencio, Colombia'),
('09','AFRICA','Tripoli asks Kyiv about Libya attack'),
('10','CLIMATE','Guterres AI-risk framework within 1 year'),
('11','AMERICAS','Tedros: lift US fuel blockade on Cuba'),
('12','TECH','Microsoft declares Code Red on AI'),
('13','MIDDLE EAST','Houthis 60 km from Aden; Hodeidah hit, 11 killed'),
('14','AFRICA','Senegal regain the AFCON 2025 title'),
('15','TECH','Tesla and SpaceX merger talks, FT'),
('16','US','CIA hack exposes unclassified data'),
('17','ASIA','Seoul jets scramble as Russian jets enter zone'),
('18','AMERICAS','US drones aid Mexico arrest of El Chapo Isidro'),
('19','MARKETS','MSCI Indonesia downgrade talks'),
('20','PACIFIC','Solomons Australia security pact'),
('21','ASIA','Malaysia repatriates 6,803 Myanmar nationals')]
for i,(num,tag,body) in enumerate(BRIEFS):
    x=20+(0 if i<11 else 497); y=842+(i if i<11 else i-11)*13
    textbox(num,x,y,20,13,bold(11),RED,maxlines=1,leading=13)
    label=tag+': '; tw=d.textlength(label,font=bold(11))
    textbox(label,x+23,y,470,13,bold(11),maxlines=1,leading=13)
    textbox(body,x+23+tw,y,466-tw,13,sans(11),maxlines=1,leading=13)
d.line((508,842,508,985),fill=RULE)
rule(994)
textbox('BBC  -  AP  -  REUTERS  -  FRANCE 24',20,1001,600,18,bold(12),NAVY,maxlines=1)
textbox('SOURCES  /  24 NOVEMBER 2026',745,1002,260,16,sans(11),GREY,maxlines=1)

im.save(base/'entry.png', optimize=True)
assert im.size==(1024,1024)
