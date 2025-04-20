import os
import django
import datetime
import requests
from io import BytesIO
import random

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Article, News, Partner, TeamMember, Contact
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            return ContentFile(response.content, name=filename)
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def create_sample_data():
    # Clear existing data
    Article.objects.all().delete()
    News.objects.all().delete()
    Partner.objects.all().delete()
    TeamMember.objects.all().delete()
    Contact.objects.all().delete()
    
    # Image URLs for articles
    article_images = [
        "https://placehold.co/800x500/70ae54/ffffff?text=Dried+Apricots",
        "https://placehold.co/800x500/70ae54/ffffff?text=Sustainable+Farming",
        "https://placehold.co/800x500/70ae54/ffffff?text=Dried+Fruit+Recipes",
    ]
    
    # Create Articles
    articles = [
        {
            'title': 'Health Benefits of Dried Apricots',
            'content': '''Dried apricots are not only delicious but also incredibly nutritious. They're packed with fiber, vitamins, and minerals that can benefit your health in numerous ways.

Rich in antioxidants, dried apricots help protect your cells from damage caused by free radicals. They're an excellent source of vitamin A, which is essential for eye health, immune function, and cell growth.

The high fiber content in dried apricots supports digestive health and can help regulate blood sugar levels. They also contain potassium, which helps maintain healthy blood pressure.

Incorporating dried apricots into your diet as a snack or adding them to salads, cereals, or baked goods can be a simple way to boost your nutrient intake.''',
        },
        {
            'title': 'Sustainable Farming Practices at Dry Fruta',
            'content': '''At Dry Fruta, we believe that the best dried fruits come from sustainably grown crops. That's why we partner with farms that prioritize environmental stewardship and sustainable agriculture practices.

Our partner farms use water conservation techniques, natural pest management, and soil health practices that reduce the need for chemical inputs. Many of our farmers implement drip irrigation systems that minimize water usage while ensuring optimal crop growth.

We support biodiversity on farms by encouraging the preservation of natural habitats around orchards and fields. This approach creates a balanced ecosystem that reduces pest problems naturally.

By choosing Dry Fruta products, you're supporting sustainable farming practices that protect the environment while producing the highest quality dried fruits available.''',
        },
        {
            'title': 'Creative Recipes Using Dried Fruits',
            'content': '''Dried fruits are incredibly versatile ingredients that can elevate both sweet and savory dishes. Here are some creative ways to incorporate our premium dried fruits into your cooking:

Breakfast Boost: Add chopped dried apricots, cranberries, or dates to your morning oatmeal or yogurt for natural sweetness and extra nutrition.

Savory Dishes: Mix dried fruits into grain salads like quinoa or couscous, or add them to tagines and stews for a sweet-savory balance.

Homemade Energy Bars: Combine dried fruits with nuts, seeds, and a bit of honey to create nutritious, portable energy bars perfect for on-the-go snacking.

Baked Goods: Incorporate dried fruits into muffins, cookies, and breads for moisture, flavor, and natural sweetness that reduces the need for added sugars.

Infused Water: Add dried fruits to water for a naturally flavored beverage that's refreshing and nutritious.

Try these ideas to enjoy the concentrated flavor and nutrition of dried fruits in new and exciting ways!''',
        }
    ]
    
    for i, article_data in enumerate(articles):
        image_url = article_images[i]
        image_name = f"article_{i+1}.jpg"
        image_content = download_image(image_url, image_name)
        
        Article.objects.create(
            title=article_data['title'],
            content=article_data['content'],
            is_published=True,
            image=image_content
        )
    
    # News image URLs
    news_images = [
        "https://placehold.co/800x500/70ae54/ffffff?text=New+Markets",
        "https://placehold.co/800x500/70ae54/ffffff?text=Organic+Certification",
    ]
    
    # Create News
    news_items = [
        {
            'title': 'Dry Fruta Expands Distribution to New Markets',
            'content': '''We're excited to announce that Dry Fruta products are now available in three new international markets! After months of preparation, our premium dried fruits can now be found in select stores across Canada, Japan, and Australia.

This expansion represents an important milestone in our company's growth and allows us to share our commitment to quality and sustainability with even more customers around the world.

"We've seen increasing demand for high-quality, naturally dried fruits without additives or preservatives," says our CEO. "These new markets appreciate our dedication to sustainable farming and traditional drying methods."

Look for Dry Fruta products in premium grocery stores and health food shops in these new locations beginning next month.''',
        },
        {
            'title': 'New Organic Certification Achieved',
            'content': '''Dry Fruta is proud to announce that we have received official organic certification for our entire product line. This certification validates our long-standing commitment to natural, chemical-free farming and processing methods.

The certification process involved rigorous evaluation of our supply chain, from the farms where our fruits are grown to our processing facilities and packaging operations. This comprehensive assessment ensures that every Dry Fruta product meets the highest standards for organic food production.

"This certification is the culmination of years of dedication to organic principles," explains our Sustainability Officer. "Our customers can have even greater confidence that they're choosing products that are good for both their health and the environment."

Look for the official organic seal on our packaging starting next month!''',
        }
    ]
    
    for i, news_data in enumerate(news_items):
        image_url = news_images[i]
        image_name = f"news_{i+1}.jpg"
        image_content = download_image(image_url, image_name)
        
        News.objects.create(
            title=news_data['title'],
            content=news_data['content'],
            is_published=True,
            image=image_content
        )
    
    # Team member photos
    team_photos = [
        "https://placehold.co/400x500/70ae54/ffffff?text=John+Martinez",
        "https://placehold.co/400x500/70ae54/ffffff?text=Emily+Chen",
        "https://placehold.co/400x500/70ae54/ffffff?text=Michael+Thompson",
        "https://placehold.co/400x500/70ae54/ffffff?text=Sophia+Rodriguez"
    ]
    
    # Create Team Members
    team_members = [
        {
            'name': 'John Martinez',
            'position': 'CEO',
            'bio': 'With over 20 years of experience in the organic food industry, John founded Dry Fruta with a vision to bring premium quality dried fruits to health-conscious consumers worldwide. His commitment to sustainable agriculture has been the driving force behind our partnerships with eco-friendly farms.',
            'order': 1
        },
        {
            'name': 'Emily Chen',
            'position': 'COO',
            'bio': 'Emily oversees all operational aspects of Dry Fruta, ensuring efficiency from farm to table. With a background in supply chain management and agricultural economics, she has developed our innovative sourcing strategy that prioritizes quality and sustainability.',
            'order': 2
        },
        {
            'name': 'Michael Thompson',
            'position': 'CFO',
            'bio': 'Michael brings financial expertise and a commitment to ethical business practices to Dry Fruta. He ensures our financial strategies align with our mission of fair trade and sustainability, while driving profitable growth that benefits all stakeholders, from farmers to consumers.',
            'order': 3
        },
        {
            'name': 'Sophia Rodriguez',
            'position': 'Manager',
            'bio': 'With a passion for sustainable food systems and digital marketing expertise, Sophia leads our marketing initiatives. She has successfully built our brand identity around quality, transparency, and environmental responsibility, connecting with health-conscious consumers globally.',
            'order': 4
        }
    ]
    
    for i, member_data in enumerate(team_members):
        image_url = team_photos[i]
        image_name = f"team_{i+1}.jpg"
        image_content = download_image(image_url, image_name)
        
        TeamMember.objects.create(
            name=member_data['name'],
            position=member_data['position'],
            bio=member_data['bio'],
            order=member_data['order'],
            photo=image_content
        )
    
    # Partner logos
    partner_logos = [
        "https://placehold.co/400x200/70ae54/ffffff?text=Green+Valley+Farms",
        "https://placehold.co/400x200/70ae54/ffffff?text=Sunlight+Orchards",
        "https://placehold.co/400x200/70ae54/ffffff?text=Berry+Good+Cooperative",
        "https://placehold.co/400x200/70ae54/ffffff?text=Natural+Packaging"
    ]
    
    # Create Partners
    partners = [
        {
            'name': 'Green Valley Farms',
            'description': 'An organic apricot farm in California that has been our trusted supplier for over a decade. Green Valley Farms specializes in sustainable farming practices that preserve soil health and biodiversity.',
            'website': 'https://example.com/greenvalley',
            'order': 1
        },
        {
            'name': 'Sunlight Orchards',
            'description': 'A family-owned date palm plantation that produces the finest Medjool dates using traditional harvesting methods and solar drying techniques.',
            'website': 'https://example.com/sunlight',
            'order': 2
        },
        {
            'name': 'Berry Good Cooperative',
            'description': 'A cooperative of small-scale farmers who grow and sustainably harvest a variety of berries that we transform into premium dried products.',
            'website': 'https://example.com/berrygood',
            'order': 3
        },
        {
            'name': 'Natural Packaging Solutions',
            'description': 'Our packaging partner who helps us develop eco-friendly, biodegradable packaging solutions that maintain product freshness while minimizing environmental impact.',
            'website': 'https://example.com/naturalpackaging',
            'order': 4
        }
    ]
    
    for i, partner_data in enumerate(partners):
        image_url = partner_logos[i]
        image_name = f"partner_{i+1}.jpg"
        image_content = download_image(image_url, image_name)
        
        Partner.objects.create(
            name=partner_data['name'],
            description=partner_data['description'],
            website=partner_data['website'],
            order=partner_data['order'],
            logo=image_content
        )
    
    # Create Contact Information
    Contact.objects.create(
        address='123 Fruit Street, Healthy City, CA 94043',
        phone='+1 (555) 123-4567',
        email='info@dryfruta.com',
        working_hours='Monday-Friday: 9:00 AM - 6:00 PM',
        map_coordinates='37.4220,-122.0841'
    )
    
    print("Sample data has been created successfully!")

if __name__ == '__main__':
    create_sample_data() 