import os
from art import SKY, qmap, intro
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root is the published site

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&family=IBM+Plex+Sans+Arabic:wght@400;600&family=IBM+Plex+Sans:wght@400;600&family=Cormorant+Garamond:wght@600&display=swap">'

GATE = '<svg class="gate" viewBox="0 0 120 120" aria-hidden="true"><path d="M22 114 V62 A38 38 0 0 1 98 62 V114 Z" fill="#FAF5EF"/><line x1="60" y1="56" x2="60" y2="84" stroke="#A88A45" stroke-width="10" stroke-linecap="round"/></svg>'
ICON = {
 'ins': '<path d="M17 3 L29 8 V16 C29 24 23 29 17 31 C11 29 5 24 5 16 V8 Z"/><path d="M12 17 l4 4 7-8"/>',
 'dist':'<path d="M4 10 L17 4 L30 10 V24 L17 30 L4 24 Z"/><path d="M4 10 L17 16 L30 10 M17 16 V30"/>',
 'ret': '<path d="M4 12 H30 L28 30 H6 Z"/><path d="M11 12 V9 a6 6 0 0 1 12 0 V12"/>',
 're':  '<path d="M6 30 V8 H20 V30 M20 14 H28 V30 M3 30 H31"/><path d="M10 13 h3 M10 18 h3 M10 23 h3 M23 19 h2 M23 24 h2"/>',
 'trn': '<path d="M3 9 H21 V24 H3 Z M21 14 H27 L31 19 V24 H21"/><circle cx="9" cy="26" r="3"/><circle cx="25" cy="26" r="3"/>',
}
icon = lambda k: f'<svg viewBox="0 0 34 34" fill="none" stroke="#A88A45" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">{ICON[k]}</svg>'

T = {
'ar': dict(
  dir='rtl', doha='الدوحة', qatar='قطر', itag='بوابتك للأعمال في قطر', skip='تخطي', title='جبر القابضة | Jabor Holding',
  desc='جبر بن عبدالرحمن آل ثاني القابضة، مجموعة قطرية تعمل في التأمين والتوزيع والتجزئة والعقار والنقل.',
  nav=[('#about','عن المجموعة'),('#qatar','لماذا قطر'),('#sectors','القطاعات'),('#companies','الشركات'),('#chairman','رئيس مجلس الإدارة'),('#contact','تواصل معنا')],
  lang=('en.html','English'), menu='القائمة',
  h1='كل الأجزاء تعمل معًا',
  lead='جبر القابضة مجموعة قطرية تجمع أعمالًا في التأمين وتوزيع السلع الاستهلاكية وشبكات التجزئة والعقار والنقل، تحت رؤية واحدة تخدم العملاء والموظفين والمجتمع.',
  cta='تعرّف على شركاتنا',
  about_eb='عن المجموعة', about_h='مجموعة قطرية بجذور عائلية',
  about_p=['تأسست جبر القابضة لتجمع شركات العائلة واستثماراتها في كيان واحد، يدير أعمالًا في قطاعات حيوية في دولة قطر.',
           'نؤمن أن نجاح كل شركة يقوّي الأخرى، وأن الثقة والعلاقات طويلة الأمد مع العملاء والشركاء هي أساس النمو.'],
  facts=[('التأمين','وساطة تأمين مستقلة'),('التوزيع','وكالات علامات استهلاكية'),('التجزئة','هايبر ماركت وشبكة متاجر'),('العقار والنقل','استثمار وخدمات لوجستية')],
  q_eb='كلمة رئيس مجلس الإدارة', q_h='قطر، أرض الفرص',
  q_p=['قطر اليوم من أكثر اقتصادات المنطقة استقرارًا وانفتاحًا. بنت قيادتها الرشيدة، على هدي رؤية قطر الوطنية ٢٠٣٠، اقتصادًا متنوعًا يقوم على بنية تحتية بمستوى عالمي، وتشريعات تحمي المستثمر وتفتح له الأبواب.',
       'والدوحة سوق نشطة تجمع بين قوة الطلب المحلي وموقع يربط الشرق بالغرب، عبر ميناء حمد ومطار حمد الدولي، وتسندها سوق مالية ناضجة في بورصة قطر وقطاع مصرفي متين.',
       'في جبر القابضة نؤمن أن الفرص الحقيقية في قطر تكمن في القطاعات التي تمس حياة الناس كل يوم: الغذاء والتجزئة والتأمين والنقل والعقار. وبابنا مفتوح لكل شريك يشاركنا هذه الثقة بقطر ومستقبلها.'],
  q_sig='جبر بن عبدالرحمن آل ثاني', q_sig2='رئيس مجلس الإدارة',
  q_pts=[('اقتصاد متين','من أعلى دخول الفرد في العالم، وتصنيف ائتماني قوي، وقطاع مصرفي راسخ.'),
         ('موقع استراتيجي','ميناء حمد ومطار حمد الدولي يربطان السوق القطري بأسواق العالم.'),
         ('بيئة منفتحة','تشريعات تتيح للمستثمر الأجنبي التملك الكامل في قطاعات عديدة، ومناطق حرة متخصصة.'),
         ('رؤية ٢٠٣٠','تنويع الاقتصاد وتمكين القطاع الخاص، وفرص نمو في الغذاء والخدمات واللوجستيات.')],
  sec_eb='القطاعات', sec_h='مجالات أعمالنا',
  sectors=[('ins','التأمين','حلول تأمين للأفراد والشركات عبر البيان لوساطة التأمين.'),
           ('dist','التوزيع','توزيع علامات تجارية عالمية للسلع الاستهلاكية في قطر.'),
           ('ret','التجزئة','شبكة متاجر وهايبر ماركت تخدم العائلات في قطر.'),
           ('re','العقار','تطوير وإدارة استثمارات عقارية.'),
           ('trn','النقل','خدمات نقل ولوجستيات محلية.')],
  co_eb='الشركات', co_h='شركات المجموعة',
  companies=[
   ('البيان لوساطة التأمين','قطاع التأمين','وسيط تأمين مستقل في قطر يقدم المشورة للأفراد والشركات، ويختار لهم أفضل التغطيات بأسعار تنافسية، ويبني معهم علاقات طويلة قائمة على الثقة.','assets/images/bayan.png','http://www.albayaninsurance.com/'),
   ('ترانسيند القابضة','التوزيع والصناعة','مجموعة شركات يعمل فيها أكثر من ١٥٠٠ موظف، في تجارة الأغذية والضيافة والصناعة والموانئ وإدارة المرافق.','assets/images/transind.jpg','http://www.transindgroup.com/'),
   ('فود بالاس','التجزئة','أقدم هايبر ماركت في المجموعة، يخدم العائلات في قطر بتشكيلة واسعة من المنتجات.','assets/images/foodpalace.jpg','http://www.foodpalaceqatar.com/'),
   ('بروفت القابضة','خدمات متنوعة','مجموعة قطرية تأسست عام ٢٠٠٨، تعمل في تأجير السيارات والليموزين والتموين والصيانة والأمن والإعلان وإدارة المرافق.','assets/images/profit%20holding.jpg','https://www.profitholding.com.qa/'),
   ('يلو للنقليات','النقل','شركة قطرية للنقل والخدمات اللوجستية تأسست عام ٢٠٢٠، تقدم حلول نقل مستدامة داخل قطر وخارجها.','assets/images/YellowTransportation.jpg','https://yloway.com/')],
  visit='زيارة الموقع ←',
  br_eb='العلامات', br_h='شركات وعلامات نفخر بها', br_subs='الشركات التابعة لترانسيند القابضة', br_list='علامات نوزّعها في قطر',
  ch_eb='رئيس مجلس الإدارة', ch_h='القائد وراء النجاح',
  ch_name='الشيخ جبر بن عبدالرحمن بن محمد بن جبر آل ثاني', ch_role='رئيس مجلس إدارة جبر القابضة',
  ch_roles=['بنك الدوحة: عضو مجلس الإدارة ورئيس لجنة المخاطر','شركة أعمال: عضو مجلس الإدارة منذ ٢٠١٧','ترانسيند القابضة: نائب رئيس مجلس الإدارة والعضو المنتدب، والشريك المدير في المجموعة وشركاتها التابعة','البيان لوساطة التأمين: المؤسس ورئيس مجلس الإدارة والعضو المنتدب','يلو للنقليات: المؤسس ورئيس مجلس الإدارة','بيركلي للاستشارات والتدريب: المؤسس والشريك المدير','باسكن روبنز: الشريك المدير','دانكن دونتس: الشريك المدير','برايم سوليوشن للاستشارات والتجارة: المؤسس والشريك المدير (التوظيف واستشارات تقنية المعلومات)','كيو آند ماكس (Q&amp;MAX): رئيس مجلس الإدارة لسلسلة من ثلاثة متاجر، كل شي من ١ إلى ٢٠ ريال','رابطة رجال الأعمال القطريين: عضو','نادي العربي: المدير العام لفريق كرة القدم سابقًا (٢٠١٦ إلى ٢٠١٩)'],
  edu=[('بكالوريوس','إدارة الأعمال، الجامعة الأوروبية في جنيف'),('دبلوم مهني','الإدارة المالية والمصرفية، الأكاديمية العربية للعلوم المالية والمصرفية'),('برنامج قيادي','برنامج القيادة للمدراء، HEC Paris في الدوحة'),('MCIPS','عضو المعهد المعتمد للمشتريات والتوريد، بريطانيا'),('PMP','محترف إدارة المشاريع، معهد PMI الأمريكي'),('IMC','شهادة إدارة الاستثمار، جمعية CFA البريطانية')],
  ct_eb='تواصل معنا', ct_h='نسعد بتواصلكم',
  ct=[('العنوان','مكتب ١٧، الطابق الثاني، مبنى ٢٥٨، شارع ٢٥٠، إشارة التضامن، الدائري الرابع، الدوحة، قطر',False),
      ('صندوق البريد','200827',True),('الهاتف','+974 4451 2100',True),('الفاكس','+974 4436 3855',True)],
  map='افتح الموقع على الخريطة', rights='جميع الحقوق محفوظة',
),
'en': dict(
  dir='ltr', doha='Doha', qatar='Qatar', itag='Your gateway to business in Qatar', skip='Skip', title='Jabor Holding | جبر القابضة',
  desc='Jabor Bin Abdulrahman Al Thani Holding, a Qatari group in insurance, distribution, retail, real estate and transport.',
  nav=[('#about','About'),('#qatar','Why Qatar'),('#sectors','Sectors'),('#companies','Companies'),('#chairman','Chairman'),('#contact','Contact')],
  lang=('index.html','العربية'), menu='Menu',
  h1='All Parts Working Together',
  lead='Jabor Holding is a Qatari group bringing together businesses in insurance, FMCG distribution, retail networks, real estate and transport, under one vision that serves customers, employees and the community.',
  cta='Explore our companies',
  about_eb='About the group', about_h='A Qatari group with family roots',
  about_p=['Jabor Holding was founded to bring the family\'s companies and investments under one roof, managing businesses in key sectors of the State of Qatar.',
           'We believe each company\'s success strengthens the others, and that trust and long-term relationships with clients and partners are the foundation of growth.'],
  facts=[('Insurance','Independent brokerage'),('Distribution','Consumer brand agencies'),('Retail','Hypermarket and stores'),('Real estate & transport','Investment and logistics')],
  q_eb="Chairman's message", q_h='Qatar, a land of opportunity',
  q_p=["Qatar today is one of the most stable and open economies in the region. Guided by Qatar National Vision 2030, its wise leadership has built a diversified economy on world-class infrastructure and laws that protect investors and open doors for them.",
       "Doha is a vibrant market that combines strong local demand with a location linking East and West through Hamad Port and Hamad International Airport, backed by a mature capital market in the Qatar Stock Exchange and a solid banking sector.",
       "At Jabor Holding, we believe Qatar's real opportunities lie in the sectors that touch people's lives every day: food, retail, insurance, transport and real estate. Our door is open to every partner who shares our confidence in Qatar and its future."],
  q_sig='Jabor bin Abdulrahman Al-Thani', q_sig2='Chairman',
  q_pts=[('A strong economy','One of the highest incomes per capita in the world, strong credit ratings and a well-established banking sector.'),
         ('A strategic location','Hamad Port and Hamad International Airport connect the Qatari market with the world.'),
         ('An open environment','Laws that allow full foreign ownership in many sectors, and specialised free zones.'),
         ('Vision 2030','Economic diversification, an empowered private sector, and growth in food, services and logistics.')],
  sec_eb='Sectors', sec_h='Where we work',
  sectors=[('ins','Insurance','Cover for individuals and companies through Al Bayan Insurance Broker.'),
           ('dist','Distribution','Distribution of global consumer brands across Qatar.'),
           ('ret','Retail','A network of stores and hypermarkets serving families in Qatar.'),
           ('re','Real estate','Development and management of property investments.'),
           ('trn','Transport','Local transport and logistics services.')],
  co_eb='Companies', co_h='Group companies',
  companies=[
   ('Al Bayan Insurance Broker','Insurance','An independent insurance broker in Qatar advising individuals and companies, placing the right cover at competitive prices, and building long-term relationships based on trust.','assets/images/bayan.png','http://www.albayaninsurance.com/'),
   ('Transind Holding','Distribution & industry','A group of companies with over 1,500 employees in food trading, hospitality, industry, ports trading and facility management.','assets/images/transind.jpg','http://www.transindgroup.com/'),
   ('Food Palace','Retail','The group\'s longest-standing hypermarket, serving families in Qatar with a wide range of products.','assets/images/foodpalace.jpg','http://www.foodpalaceqatar.com/'),
   ('Profit Holding','Diversified services','A Qatari group founded in 2008, active in car rental, limousine, catering, auto repair, security, advertising and facility management.','assets/images/profit%20holding.jpg','https://www.profitholding.com.qa/'),
   ('Yellow Transportation','Transport','A Qatari logistics company founded in 2020, providing sustainable transport and logistics services in Qatar and abroad.','assets/images/YellowTransportation.jpg','https://yloway.com/')],
  visit='Visit website →',
  br_eb='Brands', br_h='Companies and brands we are proud of', br_subs='Transind Holding subsidiaries', br_list='Brands we distribute in Qatar',
  ch_eb='Chairman', ch_h='The leader behind the success',
  ch_name='Sheikh Jabor bin Abdulrahman bin Mohamed bin Jabor Al-Thani', ch_role='Chairman, Jabor Holding',
  ch_roles=['Doha Bank: Board Member and Chair of the Risk Committee','Aamal: Board Member since 2017','Transind Holding: Vice Chairman and Managing Director, and Managing Partner in the group and its subsidiaries','Al Bayan Insurance Broker: Founder, Chairman and Managing Director','Yellow Transportation: Founder and Chairman','Berkeley Consulting (training and education): Founder and Managing Partner','Baskin Robbins: Managing Partner','Dunkin\' Donuts: Managing Partner','Prime Solution Consulting &amp; Trading: Founder and Managing Partner (recruitment and IT consulting)','Q&amp;MAX: Chairman of a chain of three stores, everything from 1 to 20 QAR','Qatari Businessmen Association: Member','Al Arabi Sports Club: former Managing Director of the football team (2016 to 2019)'],
  edu=[('BBA','Business Administration, European University, Geneva'),('Professional Diploma','Financial Management and Banking, Arab Academy for Banking and Finance'),('Leadership','Leadership Program for Managers, HEC Paris, Doha'),('MCIPS','Member, Chartered Institute of Procurement and Supply, UK'),('PMP','Project Management Professional, PMI, USA'),('IMC','Investment Management Certificate, CFA Society UK')],
  ct_eb='Contact', ct_h='Get in touch',
  ct=[('Address','Office 17, 2nd Floor, Building 258, Street 250, Al Tadamoun Signal, D-Ring Road, Doha, Qatar',False),
      ('PO Box','200827',True),('Phone','+974 4451 2100',True),('Fax','+974 4436 3855',True)],
  map='Open in Google Maps', rights='All rights reserved',
)}


# Links and logos for the chairman's roles, aligned with ch_roles order (all kept locally so they load from our own domain)
ROLE_META = [
 ('https://www.dohabank.com.qa/', ['assets/partners/dohabank.png']),
 ('https://www.aamal.com.qa/', ['assets/partners/aamal.png']),
 ('https://www.transindgroup.com/', ['assets/logos/transind-holding.webp']),
 ('https://albayaninsurance.com/', ['assets/logos/albayan.webp']),
 ('https://yloway.com/', ['assets/partners/yellow.svg']),
 ('https://berkeleyqa.com/', ['assets/partners/berkeley.png']),
 ('https://www.baskinrobbins.com/', ['assets/brands/br.webp']),
 ('https://www.dunkindonuts.com/', ['assets/brands/dunkin.webp']),
 ('https://www.primesolutionconsulting.com/', ['assets/partners/prime.png']),
 ('https://www.tiktok.com/@qmax0746', ['assets/partners/qmax.png']),
 (None, ['assets/partners/qba.png']),
 (None, ['assets/partners/alarabi.png']),
]
SUBS = ['transind-trading','transind-logistics','transind-fb','transind-realestate','food-palace','dukkan','qatar-express','transocean','almanzil','clove','balasem','burgerstop','mr-shawarma','pavati','albadia','br','dunkin']
SUB_NAMES = {'transind-trading':'Transind Trading','transind-logistics':'Transind Logistics','transind-fb':'Transind F&amp;B','transind-realestate':'Transind Real Estate','food-palace':'Food Palace','dukkan':'Dukkan','qatar-express':'Qatar Express','transocean':'Trans Ocean','almanzil':'Al Manzil','clove':'Clove','balasem':'Balasem','burgerstop':'Burger Stop','mr-shawarma':'Mr. Shawarma','pavati':'Pavati','albadia':'Al Badia','br':'Baskin Robbins','dunkin':"Dunkin' Donuts"}
BRANDS = [('coke','Coca-Cola'),('kellogs',"Kellogg's"),('frito-lay','Frito Lay'),('kdd','KDD'),('ulker','Ülker'),('nabati','Nabati'),('lacnor','Lacnor'),('albatal','Al Batal'),('almadina','Al Madina'),('alrabwah','Al Rabwah'),('artemios','Artemios'),('barakat','Barakat'),('budi','Budi'),('darina','Darina'),('domo','Domo'),('ecocare','Eco Care'),('firebull','Fire Bull'),('flamgo','Flamgo'),('kif','KIF'),('lorx','Lorx'),('luna','Luna'),('meo','Me-O'),('mochi','My Mochi'),('montana','Montana'),('mum','MUM'),('nabil','Nabil'),('oman','Oman Chips'),('original','Original'),('shokubutsu','Shokubutsu'),('tuli','Tulip'),('walimah','Al Walimah'),('yaqeen','Al Yaqeen')]
CO_LOGO = {'bayan':'assets/logos/albayan.webp','transind':'assets/logos/transind-holding.webp',
 'foodpalace':'assets/logos/food-palace.webp',
 'profit':'assets/partners/profit.png','yellow':'assets/partners/yellow.svg'}

def role_li(r, meta):
    url, logos = meta
    name, _, rest = r.partition(':')
    imgs = ''.join(f'<img src="{l}" alt="" loading="lazy" onerror="this.remove()">' for l in logos)
    nm = f'<a href="{url}" target="_blank" rel="noopener">{name}</a>' if url else name
    return f'<li><span class="lg">{imgs}</span><span><b>{nm}</b>{":" if rest else ""}{rest}</span></li>'

MAP = 'https://www.google.com/maps/search/?api=1&query=Al+Tadamoun+Signal+D-Ring+Road+Doha+Qatar'

def body(L, k):
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in L['nav'])
    facts = ''.join(f'<div class="fact"><b>{a}</b><span>{b}</span></div>' for a, b in L['facts'])
    secs = ''.join(f'<div class="sector">{icon(i)}<h3>{h}</h3><p>{p}</p></div>' for i, h, p in L['sectors'])
    cos = ''.join(
        f'<article class="co"><div class="img">' + (f'<img class="logo-img" src="{CO_LOGO[key]}" alt="{n}" loading="lazy" data-alt="{img}" onerror="if(this.dataset.alt){{this.src=this.dataset.alt;this.dataset.alt=\'\';this.className=\'\'}}else this.remove()">' if (key:=next((k for k in CO_LOGO if k in img.lower()),None)) else f'<img src="{img}" alt="{n}" loading="lazy" onerror="this.remove()">') + '</div>'
        f'<div class="body"><span class="tag">{tag}</span><h3>{n}</h3><p>{p}</p>'
        + (f'<a class="more" href="{u}" target="_blank" rel="noopener">{L["visit"]}</a>' if u else '') + '</div></article>'
        for n, tag, p, img, u in L['companies'])
    subs = ''.join(f'<li><img src="assets/logos/{s}.webp" alt="{SUB_NAMES[s]}" loading="lazy"></li>' for s in SUBS)
    brs = ''.join(f'<li><img src="assets/brands/{s}.webp" alt="{n}" loading="lazy"></li>' for s, n in BRANDS)
    roles = ''.join(role_li(r, m) for r, m in zip(L['ch_roles'], ROLE_META))
    edu = ''.join(f'<div><b>{y}</b>{t}</div>' for y, t in L['edu'])
    ct = ''.join(f'<dt>{a}</dt><dd{" class=ltr" if ltr else ""}>{b}</dd>' for a, b, ltr in L['ct'])
    return intro(L['itag'], L['title'].split('|')[0].strip(), L['skip']) + f'''
<header class="top"><div class="wrap">
  <a class="logo" href="#top"><img src="assets/logo.png" alt="{L['title']}" width="500" height="150"></a>
  <button class="menu-btn" type="button" aria-expanded="false" onclick="var n=document.querySelector('.nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">{L['menu']}</button>
  <nav class="nav">{nav}<a class="lang" href="{L['lang'][0]}">{L['lang'][1]}</a></nav>
</div></header>
<main id="top">
<div class="hero"><div class="wrap">
  <div><span class="eyebrow" style="color:#D9C38E">{L['title'].split('|')[0].strip()}</span><h1>{L['h1']}</h1><p>{L['lead']}</p><a class="cta" href="#companies">{L['cta']}</a></div>
  {GATE}
</div>{SKY}</div>
<div class="threshold"></div>

<section id="about"><div class="wrap about">
  <div><div class="head"><span class="eyebrow">{L['about_eb']}</span><h2>{L['about_h']}</h2></div>{''.join(f'<p>{p}</p>' for p in L['about_p'])}</div>
  <div><figure class="about-photo"><img src="assets/photos/zubarah.webp" alt="" loading="lazy" width="1200" height="675"></figure><div class="facts">{facts}</div></div>
</div></section>

<section id="qatar" class="qatar"><div class="wrap">
  <div class="qmsg">
    <div class="head"><span class="eyebrow">{L['q_eb']}</span><h2>{L['q_h']}</h2></div>
    <blockquote>{''.join(f'<p>{p}</p>' for p in L['q_p'])}<footer><b>{L['q_sig']}</b><span>{L['q_sig2']}</span></footer></blockquote>
  </div>
  <div class="qpts">{''.join(f'<div><b>{a}</b><span>{c}</span></div>' for a, c in L['q_pts'])}</div>
</div></section>

<section id="sectors" class="alt"><div class="wrap">
  <div class="head"><span class="eyebrow">{L['sec_eb']}</span><h2>{L['sec_h']}</h2></div>
  <div class="sectors">{secs}</div>
</div></section>

<section id="companies"><div class="wrap">
  <div class="head"><span class="eyebrow">{L['co_eb']}</span><h2>{L['co_h']}</h2></div>
  <div class="companies">{cos}</div>
</div></section>

<section id="brands" class="brands"><div class="wrap">
  <div class="head"><span class="eyebrow">{L['br_eb']}</span><h2>{L['br_h']}</h2></div>
  <h3 class="sub">{L['br_subs']}</h3><ul class="logo-grid">{subs}</ul>
  <h3 class="sub">{L['br_list']}</h3>
</div><div class="marquee"><ul class="track">{brs}{brs.replace('<li>','<li aria-hidden="true">')}</ul></div></section>

<section id="chairman" class="alt"><div class="wrap chair">
  <div class="photo"><img src="assets/images/sheikh-img-580x450.jpg" alt="{L['ch_name']}" onerror="this.remove()"></div>
  <div><div class="head" style="margin-bottom:18px"><span class="eyebrow">{L['ch_eb']}</span><h2>{L['ch_h']}</h2></div>
    <h3>{L['ch_name']}</h3><div class="role">{L['ch_role']}</div><ul class="roles">{roles}</ul><div class="edu">{edu}</div></div>
</div></section>

<div class="photo-band" role="img" aria-label="{L['doha']}"></div>

<section id="contact" class="contact"><div class="wrap grid">
  <div><div class="head"><span class="eyebrow" style="color:#D9C38E">{L['ct_eb']}</span><h2>{L['ct_h']}</h2></div><dl>{ct}</dl>
    <a class="map" href="{MAP}" target="_blank" rel="noopener">{L['map']}</a></div>
  <div class="brand">{qmap(L['doha'], L['qatar'])}</div>
</div></section>
</main>
<footer><div class="wrap"><span>© <span class="ltr">2026</span> {L['title'].split('|')[0].strip()}. {L['rights']}.</span><span class="ltr">jaborholding.com</span></div></footer>
'''

def head(L, k):
    return (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{L["title"]}</title><meta name="description" content="{L["desc"]}">'
            f'<link rel="icon" href="assets/favicon.png">{FONTS}<link rel="stylesheet" href="assets/style.css">')

for k, fn in (('ar', 'index.html'), ('en', 'en.html')):
    L = T[k]
    page = f'<!doctype html>\n<html lang="{k}" dir="{L["dir"]}">\n<head>{head(L,k)}</head>\n<body>{body(L,k)}</body>\n</html>\n'
    open(os.path.join(D, fn), 'w').write(page)

print('ok')
