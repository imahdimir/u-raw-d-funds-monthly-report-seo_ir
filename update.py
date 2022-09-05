"""

    """

##

import pandas as pd
import requests
from githubdata import GithubData


class ZipFilesUrls:
    r89 = 'https://www.seo.ir/Upload/Editor/Files/Nahade%20Mali/MutualFundReport/138946.rar'
    r90 = 'https://www.seo.ir/Upload/Editor/Files/Nahade%20Mali/MutualFundReport/139033.rar'
    r91 = 'http://seo.ir/Upload/FileGallery/SeoFiles/130128088929930930_9130.zip'
    r92 = 'http://seo.ir/Upload/FileGallery/SeoFiles/130423648640841199_Amalkard-139243.rar'
    r93 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131050114114866595_گزارش%20عملکرد%20صندوق%20ها%20در%20سال%2093.zip'
    r94 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131064817494210458_گزارش%20عملکرد%20ماهانه%20صندوق%20ها%20در%20سال%2094.zip'
    r95 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131369752430751067_1395.rar'
    r96 = 'https://www.seo.ir/Upload/FileGallery/SeoFiles/132040155169959610_1396.rar'
    r97 = 'https://seo.ir/Upload/FileGallery/SeoFiles/131998725384723074_1397.rar'
    r98 = 'https://www.seo.ir/Upload/FileGallery/SeoFiles/132324322934114261_1398.rar'
    r99 = 'https://seo.ir/Upload/FileGallery/SeoFiles/132887795198315637_1399.rar'
    r00 = 'https://seo.ir/Upload/FileGallery/SeoFiles/133013021991577171_گزارش%20عملکرد%20صندوقها%20در%20سال%20140(1).rar'
    r01 = 'https://seo.ir/Upload/FileGallery/SeoFiles/133050378565578544_1401.rar'

zfu = ZipFilesUrls()

def main():
    pass

    ##
    # 1. Get the data from the website
    zurs = []
    for ky, vl in ZipFilesUrls.__dict__.items():
        if not ky.startswith('__'):
            zurs.append({ky : vl})

    ##
    for el in zurs:
        r = requests.get(list(el.values())[0], verify = False)
        print(r.status_code)
        print(r.headers)
        if r.status_code == 200:
            fp = 'data/' + list(el.keys())[0] + '.rar'
            with open(fp, 'wb') as f:
                f.write(r.content)


    ##


    ##


    ##

##
if __name__ == "__main__":
    main()

##
# noinspection PyUnreachableCode
if False:

    pass

    ##
    u1 = 'https://github.com/imahdimir/d-TSE-Overall-Index-TEDPIX'
    r1 = GithubData(u1)
    df = r1.read_data()

    ##
    df = df.reset_index()


    ##
    df['JMonth'] = df['JDate'].astype(str).str[0:7]

    ##
    df1 = df.groupby(['JMonth']).tail(1)

    ##
    df1 = df1[df1['JDate'].ge('1398-01')]

    ##
    df1 = df1[['JMonth', 'TEDPIXClose']]

    ##
    df1.to_excel('TEDPIX.xlsx', index = False)

    ##
    from mirutil.df_utils import save_df_as_a_nice_xl as sxl

##
sxl(df1, 'TEDPIX.xlsx')
##
