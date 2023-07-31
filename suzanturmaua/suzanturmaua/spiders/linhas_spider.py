import scrapy
import pandas as pd

class LinhasSpider(scrapy.Spider):
    name = 'linhas_spider'
    start_urls = ['https://suzanturmaua.com.br/linhas/']

    def parse(self, response):
        linhas = []
        for option in response.xpath('//select[@class="search-linhas"]/option'):
            texto_da_opcao = option.xpath('normalize-space(.//text())').get()
            linhas.append(texto_da_opcao)

        # Criar um DataFrame com os dados extraídos
        df = pd.DataFrame({'Texto': linhas})

        # Salvar os dados em um arquivo XLSX
        df.to_excel('dados_linhas.xlsx', index=False, engine='openpyxl')

