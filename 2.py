introduction={
    'introduction':'Добро пожаловать в мою прекрасную,лучшую текстовую новеллу,которую вы видели',
    'introduction2':'Для начала начнем с предисторией...\n Вы обычный студент МПТ ,который едет в техникум на метро \n Вас очень сильно клонило в сон и вы решили вздремнуть..\n Вы оказываетесь в джунглях и видите протоптанные две тропинки\n Ваши действия:\n 1.Идем по первой тропинке\n 2.Идем по второй тропинке'
}
the_main_part={
    '1tropa':'Вы пошли по первой тропинке и встречаете девушку..\n Она вам говорит: Привет, меня зовут Матильда и мне нужна твоя помощь c переноской вещей в мою избушку\n Вы соглашаетесь помочь Матильде...\n После чего она вас вознаграждает особым даром предвидения \n Вы поблагодарили ее и пошли дальше \n На своем пути вы встречаете торговца \n И он предлагает вам сыграть в игру',
    '1tropa2':'Игра заключалась в угадании в какой чаше лежит монетка и в случае выйграша вам достается монетка всего 3 чаши и одна монетка\n Вы спокойно соглашаетесь.. И вот торговец начинает прятать монетку в одну из чаш и быстро их перемешивает\n Он спрашивает в какой чаше монетка?\n Вы недолго промолчали и увиделит с помощью своего дара ,где лежит монетка и спокойно забираете\n Торговец пожелал вам удачи и посоветовал придти в город ,мол нужна работа\n Ваши действия:\n 1.Последовать за ним в город\n 2.Исследовать джунгли',
    'gorod':'Вы пришли в город и устроились на работу к торговцу , продовать его товары\n Недолгим временем вы заработали себе на жизнь и сами стали торговцем ,путешествуя по миру.',
    'jungly':'Вы остались в джунглях ,исследуя их каждый вы открывали для себя всегда что-то новое и порой это было что-то магическое\n Вы собирали каждое растение , и штучки которые казались вам магическими\n Вы увидели город и направляетесь туда..\n Там вы продаете магические растения ,которые тоже казались людям магическими, из-за чего они покупали их\n И так вы стали очень богатым,популярным магическим торговцем ',
    '2tropa':'Вы пошли по второй тропинке и видете пещеру..\n там был сундук..\n Ваши действия:\n 1.Открыть сундук\n 2. Не открывать сундук и выходить из пещеры'

}
end = {
    "sunduk":' Вы решили открыть его и посмотреть что там внутри...\n Там оказались доспехи с деревянном мечом \n Вы их забираете и выходите из пещеры ,но вдруг на вас нападает стая гиен и вы спокойно отбиваетесь\n Вдруг вы замечаете не подалеку небольшую деревушку и направляетесь туда..\nТам вас встречает девушка по имени Тасья и говорит: привет,как тебя зовут,ты откуда к нам пришел?\n Ваши действия :\n 1.Меня зовут Джозаф, я не знаю как тут оказался можешь помочь освоится\n 2.Я темный мечник пришел освободить этот мир от злых духов.',
    'shutka':'"Она расхохоталась от смеха и говорит: а ты забавный малый ,фанат берсерка с улыбкой спрашивает? \n Она вам показывает маленькую деревушку ,где все жители чем-то занимаются\n Вы почувствовали приятную атмосферу и остались там жить.',
    'znakomstvo':'"Приятно познакомится с тобой ,конечно я помогу тебе освоится в нашей маленькой,скромной деревушки\n Тасья вам показала где сеют пшено, как охраняют деревню и чистят луга \n Вы остались в деревне жить долго и счастливо'
}

def start_game():
    print(introduction["introduction"])
    print(introduction["introduction2"])
    a = int(input())
    if a == 1:
        pervayatropa()
    if a ==2:
        ftorayatropa()
def pervayatropa():
    print(the_main_part["1tropa"])   
    print(the_main_part["1tropa2"])
    d = int(input())
    if d ==1:
        print(the_main_part['gorod'])
    if d == 2:
        print(the_main_part['jungly'])
def ftorayatropa():
    print(the_main_part['2tropa'])
    b = int(input())
    if b ==1:
        sunduk()
        if b ==2:
            print("Вы решили не открывать сундук и выходите из пещеры..\n Вас встречает стая гиен и вы погибаете")
def sunduk():
    print(end['sunduk'])
    c = int(input())
    if c == 1:
        derevnya()
    if c ==2:
        print(end['shutka'])
def derevnya():
    print(end['znakomstvo'])        
start_game()
