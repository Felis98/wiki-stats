import os
import sys
import math
import array
import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt

class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)
        
        with open(filename) as f:
            for line in f:
                self.n,self._nlinks=[int(x) for x in line.split()]
                break

            self._titles = []
            self._sizes = array.array('L', [0]*self.n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self.n)
            self._offset = array.array('L', [0]*(self.n+1))
            
            number_of_article=0
            
            for i in range(self.n):
                title=f.readline()
                
                self._titles.append(title.rstrip())
                linelist=list(map(int,f.readline().split()))
                self._sizes[i]=linelist[0]
                self._redirect[i]=linelist[1]

                for j in range(number_of_article, number_of_article+linelist[2]):
                    self._links[j]=int(f.readline())

                number_of_article+=linelist[2]
                if self.n>0:
                    self._offset[i+1]=self._offset[i]+linelist[2]
                    
            # TODO: прочитать граф из файла - done
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return int(self._offset[_id+1] - self._offset[_id])

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        idd=0
        for t in self._titles:
            if t==title:
                return int(idd)
            else:
                idd+=1

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        else:
            return False

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()

    # TODO: нарисовать гистограмму и сохранить в файл



if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])

    else:
        print('Файл с графом не найден')
        sys.exit(-1)

        # TODO: статистика и гистограммы
