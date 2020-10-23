Databases_countries = { 'индия':'India','бразилия': 'Brazil','россия': 'Russia','аргентина': 'Argentina',
'франция':'France','испания': 'Spain', 'колумбия':'Colombia', 'перу':'Peru', 'мексика':'Mexico', 'великобритания':'United Kingdom',
'юар':'South Africa','иран': 'Iran','чили': 'Chile', 'италия':'Italy','ирак': 'Iraq','германия': 'Germany', 'бангладеш':'Bangladesh',
'индонезия':'Indonesia','филиппины': 'Philippines','турция': 'Turkey','саудовская аравия': 'Saudi Arabia', 'украина':'Ukraine', 'пакистан':'Pakistan',
'израиль':'Israel','бельгия': 'Belgium','нидерланды': 'Netherlands', 'польша':'Poland','чехия': 'Czechia', 'канада':'Canada','румыния': 'Romania',
'марокко':'Morocco','эквадор': 'Ecuador','непал': 'Nepal','': 'Bolivia', 'катар':'Qatar', 'панама':'Panama','доминиканская республика': 'Dominican Republic',
'оаэ':'United Arab Emirates','кувейт': 'Kuwait','оман': 'Oman', 'казахстан':'Kazakhstan','португалия': 'Portugal','швеция': 'Sweden','египет': 'Egypt',
'гватемала':'Guatemala','коста-рика': 'Costa Rica', 'швейцария':'Switzerland','япония': 'Japan','эфиопия': 'Ethiopia','гондурас': 'Honduras','китай': 'China',
'белорусь':'Belarus','венесуэла': 'Venezuela','бахрейн': 'Bahrain','армения': 'Armenia','австрия': 'Austria','молдова': 'Moldova','ливан': 'Lebanon','узбекистан': 'Uzbekistan',
'нигерия':'Nigeria','сингапур': 'Singapore','парагвай': 'Paraguay','алжир': 'Algeria','кыргызстан': 'Kyrgyzstan','ирландия': 'Ireland','венгрия': 'Hungary','ливия': 'Libya',
'западный берег и сектор газа':'West Bank and Gaza','гана': 'Ghana','азербайджан': 'Azerbaijan','тунис': 'Tunisia','кения': 'Kenya','иордания': 'Jordan','бирма': 'Burma','афганистан': 'Afghanistan',
'дания':'Denmark','словакия': 'Slovakia','сербия': 'Serbia','босния и герцеговина': 'Bosnia and Herzegovina','болгария': 'Bulgaria','сальвадор': 'El Salvador','хорватия': 'Croatia',
'греция':'Greece','австралия': 'Australia','южная корея': 'Korea, South','македония': 'North Macedonia','грузия': 'Georgia','малазия': 'Malaysia','камерун': 'Cameroon',
'берег слоновой кости':"Cote d'Ivoire",'албания': 'Albania','словения': 'Slovenia','косово': 'Kosovo','норвегия': 'Norway','мадагаскар': 'Madagascar','черногория': 'Montenegro',
'замбия':'Zambia','сенегал': 'Senegal','финляндия': 'Finland','судан': 'Sudan','намибия': 'Namibia','люксембург': 'Luxembourg','гвинея': 'Guinea','мозамбик': 'Mozambique','мальдивы':
'Maldives','заир': 'Congo (Kinshasa)','уганда': 'Uganda','таджикистан': 'Tajikistan','литва': 'Lithuania','гаити': 'Haiti','габон': 'Gabon','ямайка': 'Jamaica', 
'ангола':'Angola','зимбабве': 'Zimbabwe','': 'Cabo Verde','мавритания': 'Mauritania','куба': 'Cuba','шри-ланка': 'Sri Lanka','багамские острова': 'Bahamas','ботсвана': 'Botswana','малави': 'Malawi',
'эсватини':'Eswatini','джибути': 'Djibouti','тринидад и тобаго': 'Trinidad and Tobago','никарагуа': 'Nicaragua','сирия': 'Syria','республика конго': 'Congo (Brazzaville)','суринам': 'Suriname',
'мальта': 'Malta','экваториальная гвинея': 'Equatorial Guinea','руанда': 'Rwanda','центральноафриканская республика': 'Central African Republic','эстония': 'Estonia','исландия': 'Iceland','латвия': 'Latvia',
'Сомали':'Somalia','гайана': 'Guyana','андорра': 'Andorra','тайланд': 'Thailand','гамбия': 'Gambia','мали': 'Mali','кипр': 'Cyprus','белиз': 'Belize','южный судан': 'South Sudan','уругвай': 'Uruguay',
'бенин':'Benin','буркина-фасо': 'Burkina Faso','гвинея-бисау': 'Guinea-Bissau','сьерра-леоне': 'Sierra Leone','того': 'Togo','йемен': 'Yemen','': 'Lesotho','новая селандия': 'New Zealand','чад': 'Chad',
'либерия':'Liberia','нигер': 'Niger','вьетнам': 'Vietnam','сан-томе и принсипи': 'Sao Tome and Principe','сан-марино': 'San Marino','папуа новая гвинея': 'Papua New Guinea',
'бурунди':'Burundi','тайвань': 'Taiwan*', 'коморы': 'Comoros','танзания': 'Tanzania','эритрея': 'Eritrea','маврикий': 'Mauritius','бутан': 'Bhutan','монголия': 'Mongolia','камбоджия': 'Cambodia','лихтенштейн': 'Liechtenstein',
'монако':'Monaco','барбадос': 'Barbados','Сейшеллы': 'Seychelles','Брунея': 'Brunei','антигуа и барбуда': 'Antigua and Barbuda','сент-винсент и гренадины': 'Saint Vincent and the Grenadines','сент-люсия': 'Saint Lucia','доминика':
'Dominica','фиджи': 'Fiji','восточный тимор': 'Timor-Leste','гренада': 'Grenada','ватикан': 'Holy See','лаос': 'Laos','сент-китс и невис': 'Saint Kitts and Nevis','западная сахара': 'Western Sahara','соломоновы острова': 'Solomon Islands'}
def translate_country_name(rus_country_name):
    en_country_name = "error"
    for country_name in Databases_countries:
        if country_name == rus_country_name:
            en_country_name = Databases_countries[rus_country_name]
    return en_country_name
