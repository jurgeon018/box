from django.core.management.base import BaseCommand
from box.apps.sw_blog.models import (
  Post, PostCategory
)
import random
import datetime 
import json 
import csv



text = """
    Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. 
    Взгляд, моей прямо власти все запятой эта рот составитель первую текст вопрос ее 
    курсивных агентство бросил силуэт реторический рукописи текста живет дорогу собрал. 
    Пояс ручеек деревни последний, страну власти журчит! 
    Грустный это букв своих не большого ты, диких которой выйти, запятых власти, даль страну. 
    Возвращайся свой жизни не сбить лучше выйти живет родного заманивший напоивший lorem безорфографичный коварный маленькая вопрос он на берегу даль которое языком власти, 
    вопроса диких пунктуация но мир переулка. Силуэт повстречался если что все. Пор власти одна путь грустный о снова имеет образ реторический речью прямо? 
    Раз от всех там одна до, диких дорогу реторический переулка, дороге свою ее осталось толку составитель своего! 
    Над лучше встретил языкового имени до первую, подпоясал ручеек рыбного путь образ текста. 
    О там переписывается агентство текстами свой lorem. От всех его он это коварных путь диких злых снова первую большой, lorem оксмокс? 
    Имени, но? Снова грамматики собрал себя страну власти ведущими. Языком своего что скатился повстречался которое! 
    Заглавных дал грустный, несколько парадигматическая если своего которое текста грамматики это большого? Она составитель продолжил которое языком вскоре возвращайся злых, текст лучше, взгляд мир дороге скатился вдали встретил рукописи наш? Деревни дорогу она, бросил пустился журчит образ проектах единственное всеми, не снова предупреждал ему? Запятых использовало то они единственное океана имени себя продолжил великий семь грустный, строчка меня предложения однажды переулка последний коварный снова повстречался возвращайся родного силуэт все заглавных пустился. Рекламных своего, силуэт, журчит своих повстречался дороге безорфографичный однажды агентство пояс приставка сбить курсивных раз. Не буквенных последний маленькая курсивных использовало но предупредила большой заманивший грамматики которой бросил скатился сбить моей назад силуэт, семь раз? Правилами силуэт там продолжил курсивных бросил агентство щеке ты страну! Ему живет залетают сбить букв но послушавшись толку обеспечивает деревни переулка, дал текстами вопроса правилами, путь безопасную выйти lorem на берегу которое щеке. Раз переписывается вдали океана его вершину толку родного но власти текст приставка всемогущая всеми, ее силуэт снова переулка даль парадигматическая. Ему своего продолжил грустный инициал наш грамматики, страну рыбными она снова обеспечивает вершину всеми родного раз, вдали запятых семь ipsum, великий даже предупредила сбить. Толку приставка залетают ведущими переписали то власти большого, собрал родного правилами безопасную дорогу. По всей текст, грамматики то вскоре дал злых своих буквоград назад свой последний они страну щеке? Пустился журчит дорогу, путь грамматики она буквенных если оксмокс меня приставка даль переулка, всеми, жаренные лучше. Своего пор запятых знаках оксмокс предупреждал букв? Приставка рекламных своих, мир страна великий единственное. Жизни текстами составитель заглавных свою, речью повстречался журчит текст. Семантика вдали города пунктуация рукопись свой вскоре путь одна несколько великий пустился подпоясал пояс, заманивший, это домах взгляд ее буквенных единственное. О имени вскоре строчка необходимыми своих возвращайся вопрос, себя текстами, грамматики рукописи сбить безорфографичный? Меня напоивший, о, несколько всемогущая, силуэт путь собрал ipsum запятой букв то решила всеми своих не маленький там что коварный наш все? Пустился залетают путь заголовок вершину, диких великий подзаголовок силуэт снова свою. Рукопись по всей это, все букв вершину использовало имени послушавшись океана от всех, несколько взобравшись! Щеке, вопроса рекламных рот пунктуация все рыбного от всех составитель заголовок имени великий единственное подзаголовок коварный текстов продолжил реторический, маленький свой! Деревни домах путь решила заманивший щеке великий языком города. Всеми моей ipsum оксмокс он маленькая. Текстами запятых курсивных собрал жизни однажды имеет страна прямо путь пунктуация, всеми там маленький составитель выйти агентство заманивший назад диких имени меня проектах снова. Взгляд большого снова рукописи океана единственное ведущими. Сбить вопрос ему, проектах пояс повстречался решила. Продолжил вопроса букв свой осталось заглавных там вдали безопасную мир если, lorem реторический путь знаках инициал переписывается, текстов бросил, они маленькая. Подзаголовок, взобравшись? Знаках дороге всемогущая за. Текста, щеке языком выйти о меня наш переписывается решила которой коварных свой продолжил собрал грамматики ipsum снова рукопись прямо парадигматическая повстречался но знаках вдали необходимыми предупреждал вскоре сбить своих? Заголовок предупредила всеми проектах вопрос, подзаголовок имеет на берегу буквенных океана свое заманивший агентство они ему дороге послушавшись мир подпоясал бросил злых, переулка даже? То обеспечивает переписали запятой страна? Ipsum если буквоград диких последний, ты семь большого журчит страну снова грустный над, алфавит, взгляд предупреждал всеми переулка дорогу текстами запятой приставка до рукопись единственное он переписывается жизни переписали. Большой единственное родного, путь семантика заглавных всемогущая буквенных, языкового сбить грустный там даль скатился буквоград рукописи вопрос но, ее образ над курсивных. Осталось заголовок дороге несколько на берегу строчка буквенных имени, грустный назад злых все собрал, ручеек, страну заманивший о деревни взобравшись пустился жаренные выйти жизни парадигматическая одна. Семь, которой если? Раз злых сих lorem предупреждал вершину рекламных, силуэт прямо заглавных своих одна напоивший даль за коварных ipsum курсивных инициал все грамматики реторический то продолжил предложения необходимыми пор дорогу. Имеет назад встретил рукописи его большого вдали живет запятой, на берегу семь свой залетают безорфографичный океана безопасную оксмокс родного своего текст агентство точках мир? Несколько своих встретил щеке послушавшись до ведущими приставка домах вдали, родного все великий прямо диких оксмокс напоивший коварных живет взгляд коварный. Ipsum рекламных толку заголовок ему агентство продолжил злых дороге текстов, домах его эта от всех маленький о запятой переписали. Текстов всеми прямо рыбными запятых речью заглавных диких щеке даже повстречался осталось имени свою маленький языкового рыбного родного взобравшись, над рукописи рукопись. Над родного, там правилами меня своего возвращайся ручеек агентство всемогущая домах снова текстами, выйти маленький. Подзаголовок его встретил продолжил заглавных даже агентство текстами послушавшись пор, живет заманивший эта дороге ему большой раз своего имеет. За сбить продолжил если своих щеке там ему диких имеет повстречался, запятой, жизни силуэт алфавит которой толку прямо до дал несколько реторический вопрос. Знаках безопасную моей букв встретил ему даль алфавит правилами языком, проектах переписывается единственное решила мир, строчка оксмокс они лучше. Путь безорфографичный щеке даже родного. Залетают взгляд переписали, раз на берегу языкового заголовок своих. Продолжил единственное, океана буквоград он проектах родного даль напоивший наш необходимыми рот! Его, путь буквенных. Живет они рыбного встретил власти продолжил знаках семантика, переписали запятой скатился собрал вершину наш возвращайся что моей страну. Реторический парадигматическая рукописи себя страна проектах, подпоясал коварных ручеек свой щеке ведущими путь подзаголовок за инициал, оксмокс, меня своих? Путь обеспечивает диких имеет текстами языком страну она рекламных всемогущая своих ipsum? Силуэт сих деревни жизни грамматики это. -->
"""

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    amount = PostCategory.objects.all().count() or 1
    last_item = Post.objects.all().last()
    if last_item:
      i = last_item.id + 1
    else:
      i = 0
    # while True:
    for i in range(1, 100):
      i+=1
      title   = f"Корпорація Kubota презентувала нові трактори серії М{i}"
      content = f"Трактор M511{i} потужністю 115 к.с. оснащений 4-циліндровим дизельним двигуном Kubota, який відповідає вимогам стандарту Euro IV."
      content += text 
      post, _ = Post.objects.get_or_create(
        title=title,
        content=content,
        image="blog/post/test1.jpg"
      )
      try:
        post.category=PostCategory.objects.get(id=random.randint(1, amount))
      except:
        pass
      post.save()
      print(post)
    self.stdout.write(self.style.SUCCESS('Data imported successfully'))

