import requests
from bs4 import BeautifulSoup


def about():
    url = "https://pratham.org/"

    html_text = requests.get(url).text


    soup = BeautifulSoup(html_text, 'lxml')
    about = soup.find('div', class_='panel-widget-style panel-widget-style-for-w65e964465c70a-0-1-0')
    about1 = about.find('div', class_='textwidget').text
    with open("info/web_scrapped1.txt", 'w') as f:
        f.write(about1)
    print("file_saved")





def recognition():
    url2 = "https://pratham.org/about/recognition/"
    html1_text = requests.get(url2).text
    # print(html_text)

    soup = BeautifulSoup(html1_text, 'lxml')
    recognition = soup.find('div', class_= 'siteorigin-widget-tinymce textwidget').text
    
    with open("info/web_scrapped2.txt", 'w') as f:
        f.write(recognition)
    print("file_saved2")

    award_list = soup.find_all('li', class_= "listing-item")
    for i,award in enumerate(award_list):
        a1 = award.find('p').text
        a2 = award.find('span').text
        with open(f'info/{i}.txt', 'w') as f:
            # f.write(a1)
            f.write(f'{a1} : explaination: {a2}')
    print("file_saved3")


def education():
    url3 = "https://pratham.org/programs/education/"
    html2_text = requests.get(url3).text


    soup1 = BeautifulSoup(html2_text, 'lxml')
    edu = soup1.find('div', class_="so-widget-sow-editor so-widget-sow-editor-base")
    educ = edu.find('p').text
    with open("info/web_scrapped3.txt", 'w') as f:
        f.write(educ)
    print("file_saved4")


def founder():
    url4 = "https://pratham.org/2019/05/21/dr-rukmini-banerji-3/"

    html3_text = requests.get(url4).text


    soup2 = BeautifulSoup(html3_text, 'lxml')
    founder1 = soup2.find('div', class_= "kc-elm kc-css-338946 kc_text_block").text
    with open("info/web_scrapped4.txt", 'w') as f:
        f.write(founder1)
    print('file_saved5')

def second_chance():
    url5 = "https://www.pratham.org/programs/education/beyond-elementary/"
    html4_text = requests.get(url5).text
    soup3 = BeautifulSoup(html4_text, 'lxml')
    second_chance = soup3.find('div', class_="kc-elm kc-css-796833 kc_text_block white-box table-box introBoxCol").text
    with open("info/web_scrapped5.txt", 'w') as f:
        f.write(second_chance)
    print('file_saved6')


#about()
#founder()
recognition()
#education()
#second_chance()