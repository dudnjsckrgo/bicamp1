from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
from pandas import DataFrame
class Service:
    def __init__(self):
        self.soup = None
        self.len_mytarget = None
        self.mytarget = None
        self.myfolder =None
        self.weekday_dict= None


    def bugs_music(self):
        pass
    def naver_movie(self):
        pass
    # 이 메소드는 url을 받아서 soup 속성을 초기화한다.
    def get_url(self,url):
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        response = urlopen(url)
        self.soup = BeautifulSoup(response, myparser)
        return type(self.soup)

    # 이 메소드는 folderName을 가진 이름의 파일을 현재 폴더 하위에 생성한다.
    def create_folder_weekend(self,folderName):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        self.weekday_dict=weekday_dict
        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        
        myfolder = './'+folderName +'/' # 유닉스 기반은 '/'이 구분자
        self.myfolder = myfolder
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    # mysrc 이미지파일의 url myweekday는 요일정 mytitle에 이미지 제목이 들어간다.
    @staticmethod
    def saveFile(myfolder, mysrc:str , myweekday:str, mytitle :str,weekday_dict):

        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        # print(mysrc)
        # print(filename)

        myfile = open(filename, mode='wb')  # wb : write binary
        myfile.write(image_file.read())  # 바이트 형태로 저장
        myfile.close()
        # soup의 태그와 속성을 이용해 target을 정하고 타겟의 길이를 프린트한다.


    def setting_target(self,*args):
        print(len(args))
        if len(args)==2:

            self.mytarget = self.soup.find_all(args[0], attrs={'class': args[1]})
        if len(args)==1:
            self.mytarget = self.soup.find_all(args[0])
        self.len_mytarget=  len(self.mytarget)
        print(self.mytarget)
        print("타겟의 길이:",self.len_mytarget)

    def loop_fun(self,replace_str,mycolumns,filename):

        mylist = []  # 데이터를 저장할 리스트

        for abcd in self.mytarget:
            myhref = abcd.find('a').attrs['href']
            print('myhref:', myhref)
            print('_' * 30)
            myhref = myhref.replace( replace_str , '')
            result = myhref.split('&')
            print('myhref:',myhref)
            print('_'*30)
            print('result:',result)
            print('_'*30)
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            print('mytitleid:',mytitleid)
            print('_' * 30)
            print("myweekday:",myweekday)
            print('_' * 30)
            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            print(mytitle)

            mysrc = imgtag.attrs['src']
            # print(mysrc)
            myfolder=self.myfolder
            weekday_dict=self.weekday_dict
            Service.saveFile(myfolder,mysrc, myweekday, mytitle,weekday_dict)

            # break

            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)
            break
        Service.saveCsv(mycolumns,mylist,filename)

    @staticmethod
    def saveCsv(mycolumns,mylist,filename):
        myframe = DataFrame(mylist, columns=mycolumns)

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + '파일로 저장됨')

        print('finished')
    def loop_fun2(self,mycolumns,filename):
        mytrs=self.mytarget
        no = 0  # 순서를 의미하는 번호
        totallist = []  # 전체를 저장할 리스트
        for one_tr in mytrs:
            # print(one_tr)
            # print('@'*30)

            title = ''
            up_down = ''  # 순위 변동 설명 문구

            mytd = one_tr.find('td', attrs={'class': 'title'})
            if mytd is not None:
                no += 1
                newno = str(no).zfill(2)

                mytag = mytd.find('div', attrs={'class': 'tit3'})
                title = mytag.a['title']  # title 속성에도 위의 a.string과 마찬가지로 제목이 담겨있다

                # 순위 변동 부분 파싱
                mytd = one_tr.select_one('td:nth-of-type(3)')  # 세 번째 td를 선택
                myimg = mytd.find('img')
                if myimg.attrs['alt'] == 'up':
                    up_down = '상승'
                elif myimg.attrs['alt'] == 'down':
                    up_down = '강등'
                else:
                    up_down = '불변'

                change = one_tr.find('td', attrs={'class': 'range ac'})
                if change is None:
                    change = '신규 진입'
                else:
                    change = change.string

                # print(newno + '/' + title + '/' + up_down + '/' + change)

                # csv로 저장
                totallist.append((newno, title, up_down, change))

        Service.saveCsv(mycolumns,totallist,filename)
