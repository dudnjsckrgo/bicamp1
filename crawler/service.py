class Service:
    def __init__(self):
        pass
    def bugs_music(self):
        pass
    def naver_movie(self):
        pass
    def naver_cartoon(self,url):
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        print(type(soup))
    def creat_folder_weekend(self):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        import os, shutil
        myfolder = 'd:\\imsi\\' # 유닉스 기반은 '/'이 구분자

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