"""

    """

import requests
from githubdata import GitHubDataRepo as GHDR

class RepoUrls :
    cur = 'https://github.com/imahdimir/u-rd0-funds-monthly-report-seo_ir'
    trg = 'https://github.com/imahdimir/rd0-funds-monthly-report-seo_ir'

ru = RepoUrls()

class ZipFilesUrls :
    r1389 = 'https://www.seo.ir/Upload/Editor/Files/Nahade%20Mali/MutualFundReport/138946.rar'
    r1390 = 'https://www.seo.ir/Upload/Editor/Files/Nahade%20Mali/MutualFundReport/139033.rar'
    r1391 = 'http://seo.ir/Upload/FileGallery/SeoFiles/130128088929930930_9130.zip'
    r1392 = 'http://seo.ir/Upload/FileGallery/SeoFiles/130423648640841199_Amalkard-139243.rar'
    r1393 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131050114114866595_گزارش%20عملکرد%20صندوق%20ها%20در%20سال%2093.zip'
    r1394 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131064817494210458_گزارش%20عملکرد%20ماهانه%20صندوق%20ها%20در%20سال%2094.zip'
    r1395 = 'http://seo.ir/Upload/FileGallery/SeoFiles/131369752430751067_1395.rar'
    r1396 = 'https://www.seo.ir/Upload/FileGallery/SeoFiles/132040155169959610_1396.rar'
    r1397 = 'https://seo.ir/Upload/FileGallery/SeoFiles/131998725384723074_1397.rar'
    r1398 = 'https://www.seo.ir/Upload/FileGallery/SeoFiles/132324322934114261_1398.rar'
    r1399 = 'https://seo.ir/Upload/FileGallery/SeoFiles/132887795198315637_1399.rar'
    r1400 = 'https://seo.ir/Upload/FileGallery/SeoFiles/133013021991577171_گزارش%20عملکرد%20صندوقها%20در%20سال%20140(1).rar'
    r1401 = 'https://seo.ir/Upload/FileGallery/SeoFiles/133050378565578544_1401.rar'

zfu = ZipFilesUrls()

def main() :
    pass

    ##

    zurs = []
    for ky , vl in ZipFilesUrls.__dict__.items() :
        if not ky.startswith('__') :
            zurs.append({
                    ky : vl
                    })

    ##
    zurs = zurs[-2 :]

    ##
    rp_trg = GHDR(ru.trg)
    rp_trg.clone_overwrite()

    data_dir = rp_trg.local_path

    ##
    for el in zurs :

        print(list(el.keys())[0])

        r = requests.get(list(el.values())[0] , verify = False)

        print(r.status_code)
        print(r.headers)

        if r.status_code == 200 :
            fp = data_dir / str(list(el.keys())[0] + '.rar')
            with open(fp , 'wb') as f :
                f.write(r.content)
                print('Downloaded:' , fp)

    ##
    msg = 'udated by: '
    msg += ru.cur

    rp_trg.commit_and_push(msg)

    ##
    rp_trg.rmdir()

##


if __name__ == "__main__" :
    main()
    print()

##

# noinspection PyUnreachableCode
if False :
    pass

    ##

    ##
