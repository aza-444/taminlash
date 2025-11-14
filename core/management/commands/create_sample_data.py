from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from core.models import CarouselSlide, QuickLink, GovernmentLink, CompanyHistory
from news.models import NewsCategory, News, Video
from powerplants.models import PowerPlant, KeyIndicator
from contact.models import Survey, SurveyChoice, HelplineStats


class Command(BaseCommand):
    help = 'Create sample data for tpp.uz clone'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        QuickLink.objects.get_or_create(
            order=1,
            defaults={'title': "Kasaba uyushmasi", 'link': "/admin/"}
        )
        
        QuickLink.objects.get_or_create(
            order=2,
            defaults={'title': "Korrupsiyaga qarshi chora-tadbirlar", 'link': "/admin/"}
        )
        
        QuickLink.objects.get_or_create(
            order=3,
            defaults={'title': "Tenderlar va auktsionlar", 'link': "/admin/"}
        )
        
        QuickLink.objects.get_or_create(
            order=4,
            defaults={'title': "Ma'lumot so'rash tartibi", 'link': "/admin/"}
        )
        
        QuickLink.objects.get_or_create(
            order=5,
            defaults={'title': "Vakansiyalar", 'link': "/admin/"}
        )
        
        QuickLink.objects.get_or_create(
            order=6,
            defaults={'title': "Ochiq ma'lumotlar", 'link': "/admin/"}
        )
        
        KeyIndicator.objects.get_or_create(
            order=1,
            defaults={'title': "O'rnatilgan quvvat", 'value': "8,764", 'unit': "MWh", 'year': 2024}
        )
        
        KeyIndicator.objects.get_or_create(
            order=2,
            defaults={'title': "Elektr energiyasi ishlab chiqarildi", 'value': "32", 'unit': "mlrd kWh", 'year': 2024}
        )
        
        KeyIndicator.objects.get_or_create(
            order=3,
            defaults={'title': "Mavjud quvvat", 'value': "6,774", 'unit': "MWh", 'year': 2024}
        )
        
        KeyIndicator.objects.get_or_create(
            order=4,
            defaults={'title': "Issiqlik energiyasi ishlab chiqarildi", 'value': "11.1", 'unit': "mln Gkal", 'year': 2024}
        )
        
        HelplineStats.objects.get_or_create(
            id=1,
            defaults={
                'total_calls': 395,
                'rating_5': 181,
                'rating_4': 66,
                'rating_3': 45,
                'rating_2': 32,
                'rating_1': 71
            }
        )
        
        CompanyHistory.objects.get_or_create(
            year_start=1924,
            defaults={'content': "O'zbekiston energetika sektori - iqtisodiyotning eng muhim, asosiy, yuqori texnologiyali sohasi bo'lib, boshqa barcha iqtisodiy tarmoqlar va sub'ektlarning samarali faoliyatini ta'minlaydi. 1924-yildan buyon O'zbekiston energetika tizimi rivojlanib kelmoqda."}
        )
        
        survey1, _ = Survey.objects.get_or_create(
            step_number=1,
            defaults={'question': "So'rovda qatnashmoqchimisiz?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey1, order=1, defaults={'choice_text': "Ha"})
        SurveyChoice.objects.get_or_create(survey=survey1, order=2, defaults={'choice_text': "Yo'q"})
        
        survey2, _ = Survey.objects.get_or_create(
            step_number=2,
            defaults={'question': "IES xizmatlari sifatini qanday baholaysiz?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey2, order=1, defaults={'choice_text': "A'lo"})
        SurveyChoice.objects.get_or_create(survey=survey2, order=2, defaults={'choice_text': "Yaxshi"})
        SurveyChoice.objects.get_or_create(survey=survey2, order=3, defaults={'choice_text': "Qoniqarli"})
        SurveyChoice.objects.get_or_create(survey=survey2, order=4, defaults={'choice_text': "Yomon"})
        
        survey3, _ = Survey.objects.get_or_create(
            step_number=3,
            defaults={'question': "Elektr ta'minoti barqarorligini qanday baholaysiz?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey3, order=1, defaults={'choice_text': "Juda yaxshi"})
        SurveyChoice.objects.get_or_create(survey=survey3, order=2, defaults={'choice_text': "Yaxshi"})
        SurveyChoice.objects.get_or_create(survey=survey3, order=3, defaults={'choice_text': "Qoniqarli"})
        SurveyChoice.objects.get_or_create(survey=survey3, order=4, defaults={'choice_text': "Yaxshilanishi kerak"})
        
        survey4, _ = Survey.objects.get_or_create(
            step_number=4,
            defaults={'question': "Kompaniya saytining foydaliligi qanday?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey4, order=1, defaults={'choice_text': "Juda foydali"})
        SurveyChoice.objects.get_or_create(survey=survey4, order=2, defaults={'choice_text': "Foydali"})
        SurveyChoice.objects.get_or_create(survey=survey4, order=3, defaults={'choice_text': "O'rtacha"})
        SurveyChoice.objects.get_or_create(survey=survey4, order=4, defaults={'choice_text': "Kamfoydali"})
        
        survey5, _ = Survey.objects.get_or_create(
            step_number=5,
            defaults={'question': "Hodimlarning xizmat ko'rsatishi qanday?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey5, order=1, defaults={'choice_text': "Ajoyib"})
        SurveyChoice.objects.get_or_create(survey=survey5, order=2, defaults={'choice_text': "Yaxshi"})
        SurveyChoice.objects.get_or_create(survey=survey5, order=3, defaults={'choice_text': "Qoniqarli"})
        SurveyChoice.objects.get_or_create(survey=survey5, order=4, defaults={'choice_text': "Qoniqarsiz"})
        
        survey6, _ = Survey.objects.get_or_create(
            step_number=6,
            defaults={'question': "Kompaniya yangilanishlaridan xabardormisiz?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey6, order=1, defaults={'choice_text': "Ha, doimo"})
        SurveyChoice.objects.get_or_create(survey=survey6, order=2, defaults={'choice_text': "Ba'zan"})
        SurveyChoice.objects.get_or_create(survey=survey6, order=3, defaults={'choice_text': "Kamdan-kam"})
        SurveyChoice.objects.get_or_create(survey=survey6, order=4, defaults={'choice_text': "Yo'q"})
        
        survey7, _ = Survey.objects.get_or_create(
            step_number=7,
            defaults={'question': "Kompaniyani do'stlaringizga tavsiya qilasizmi?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey7, order=1, defaults={'choice_text': "Albatta"})
        SurveyChoice.objects.get_or_create(survey=survey7, order=2, defaults={'choice_text': "Ehtimol ha"})
        SurveyChoice.objects.get_or_create(survey=survey7, order=3, defaults={'choice_text': "Ehtimol yo'q"})
        SurveyChoice.objects.get_or_create(survey=survey7, order=4, defaults={'choice_text': "Yo'q"})
        
        survey8, _ = Survey.objects.get_or_create(
            step_number=8,
            defaults={'question': "Umumiy bahoyingiz nechta yulduzdan iborat?", 'is_active': True}
        )
        SurveyChoice.objects.get_or_create(survey=survey8, order=1, defaults={'choice_text': "5 yulduz"})
        SurveyChoice.objects.get_or_create(survey=survey8, order=2, defaults={'choice_text': "4 yulduz"})
        SurveyChoice.objects.get_or_create(survey=survey8, order=3, defaults={'choice_text': "3 yulduz"})
        SurveyChoice.objects.get_or_create(survey=survey8, order=4, defaults={'choice_text': "2 yulduz"})
        SurveyChoice.objects.get_or_create(survey=survey8, order=5, defaults={'choice_text': "1 yulduz"})
        
        news_cat, _ = NewsCategory.objects.get_or_create(
            slug='yangiliklar',
            defaults={'name': "Yangiliklar"}
        )
        
        tech_cat, _ = NewsCategory.objects.get_or_create(
            slug='texnologiyalar',
            defaults={'name': "Texnologiyalar"}
        )
        
        News.objects.get_or_create(
            slug='xalqaro-hamkorlik-loyihasi',
            defaults={
                'title': "Energetika sohasida yana bir xalqaro hamkorlik loyihasi muvaffaqiyatli yakunlandi",
                'category': news_cat,
                'content': "<p>Energetika sohasidagi xalqaro hamkorlik loyihasi muvaffaqiyatli yakunlandi. Loyiha doirasida zamonaviy energiya tejovchi texnologiyalar joriy etildi.</p>",
                'excerpt': "Energetika sohasidagi xalqaro hamkorlik loyihasi muvaffaqiyatli yakunlandi",
                'published_date': timezone.now().date(),
                'is_featured': True
            }
        )
        
        News.objects.get_or_create(
            slug='yangi-gaz-turbinasi',
            defaults={
                'title': "Yangi gaz turbinasi ishga tushirildi",
                'category': tech_cat,
                'content': "<p>Navoi IES da yangi 650 MW quvvatli gaz turbinasi ishga tushirildi. Bu energiya samaradorligini 40% ga oshiradi.</p>",
                'excerpt': "Navoi IES da yangi zamonaviy gaz turbinasi ishga tushirildi",
                'published_date': (timezone.now() - timedelta(days=3)).date(),
                'is_featured': True
            }
        )
        
        News.objects.get_or_create(
            slug='modernizatsiya-ishlari',
            defaults={
                'title': "Syrdaryo IES da modernizatsiya ishlari davom etmoqda",
                'category': news_cat,
                'content': "<p>Syrdaryo IES da keng ko'lamli modernizatsiya ishlari olib borilmoqda. Loyiha 2025 yil oxirida yakunlanishi rejalashtirilgan.</p>",
                'excerpt': "Syrdaryo IES modernizatsiya loyihasi muvaffaqiyatli davom etmoqda",
                'published_date': (timezone.now() - timedelta(days=7)).date(),
                'is_featured': False
            }
        )
        
        News.objects.get_or_create(
            slug='ekologik-standartlar',
            defaults={
                'title': "IES korxonalari yangi ekologik standartlarga o'tdi",
                'category': news_cat,
                'content': "<p>Barcha IES korxonalari xalqaro ekologik standartlarga muvofiq ishlashni boshladi.</p>",
                'excerpt': "Yangi ekologik standartlar joriy etildi",
                'published_date': (timezone.now() - timedelta(days=10)).date(),
                'is_featured': False
            }
        )
        
        News.objects.get_or_create(
            slug='yoshlar-bilan-uchrashuv',
            defaults={
                'title': "IES rahbariyati yoshlar bilan uchrashdi",
                'category': news_cat,
                'content': "<p>IES bosh direktori yoshlar bilan uchrashuv o'tkazdi va kelajak rejalari haqida gapirdi.</p>",
                'excerpt': "Yoshlar bilan mazmunli suhbat",
                'published_date': (timezone.now() - timedelta(days=14)).date(),
                'is_featured': False
            }
        )
        
        PowerPlant.objects.get_or_create(
            name="Toshkent IES",
            defaults={
                'plant_type': 'TPS',
                'capacity': 1780,
                'location': "Toshkent",
                'latitude': 41.2995,
                'longitude': 69.2401,
                'description': "<p>Toshkent shahrining eng yirik issiqlik elektr stansiyasi</p>",
                'established_year': 1963,
                'is_active': True
            }
        )
        
        PowerPlant.objects.get_or_create(
            name="Syrdaryo IES",
            defaults={
                'plant_type': 'TPS',
                'capacity': 3200,
                'location': "Sirdaryo viloyati",
                'latitude': 40.3833,
                'longitude': 68.7167,
                'description': "<p>O'zbekistonning eng yirik elektr stansiyasi</p>",
                'established_year': 1977,
                'is_active': True
            }
        )
        
        PowerPlant.objects.get_or_create(
            name="Navoi IES",
            defaults={
                'plant_type': 'TPS',
                'capacity': 1250,
                'location': "Navoi viloyati",
                'latitude': 40.0844,
                'longitude': 65.3792,
                'description': "<p>Navoi viloyatining asosiy elektr ta'minoti manbai</p>",
                'established_year': 1972,
                'is_active': True
            }
        )
        
        CarouselSlide.objects.get_or_create(
            order=1,
            defaults={'title': "O'zbekiston Issiqlik Elektr Stantsiyalari", 'link': "/"}
        )
        
        CarouselSlide.objects.get_or_create(
            order=2,
            defaults={'title': "Barqaror energiya - yuksak hayot sifati", 'link': "/news/"}
        )
        
        CarouselSlide.objects.get_or_create(
            order=3,
            defaults={'title': "Zamonaviy texnologiyalar - kelajak sari", 'link': "/"}
        )
        
        CarouselSlide.objects.get_or_create(
            order=4,
            defaults={'title': "Ekologik toza energiya yechimlar", 'link': "/"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=1,
            defaults={'name': "O'zbekiston Respublikasi Prezidenti", 'url': "https://president.uz"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=2,
            defaults={'name': "Vazirlar Mahkamasi", 'url': "https://gov.uz"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=3,
            defaults={'name': "Energetika vazirligi", 'url': "https://minenergy.uz"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=4,
            defaults={'name': "Yagona interaktiv davlat xizmatlari portali", 'url': "https://my.gov.uz"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=5,
            defaults={'name': "Davlat xizmatlari markazi", 'url': "https://dxm.uz"}
        )
        
        GovernmentLink.objects.get_or_create(
            order=6,
            defaults={'name': "Axborot xavfsizligi markazi", 'url': "https://cert.uz"}
        )
        
        Video.objects.get_or_create(
            title="IES yangiliklari 2024",
            defaults={
                'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                'description': 'IES yangiliklari va yutuqlaridan video reportaj',
                'published_date': timezone.now().date()
            }
        )
        
        Video.objects.get_or_create(
            title="Yangi IES qurilishi",
            defaults={
                'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                'description': 'Yangi issiqlik elektr stansiyasi qurilishidan lavhalar',
                'published_date': (timezone.now() - timedelta(days=5)).date()
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
