# Equalização de Histogramas

## Desenvolvido por [Hernandes Macedo](https://github.com/hernandesmacedo) & [Heitor Galdino](https://github.com/h80r)
  &nbsp;
### [Vídeo de apresentação do projeto](https://youtu.be/cspS9S2HCPM)
  &nbsp;

## Descrição
Nesse projeto há a implementação de um algoritmo de equalização de histogramas para imagens em níveis de cinza. Essa técnica visa obter uma melhor variância no histograma de cores da imagem, gerando uma outra com maior contraste.

## Exemplos

  ![Imagem com Histograma Equalizado](https://lh3.googleusercontent.com/IQ_hWkxqguI9xGwkGJihFOpS9_NlnwV50272PR_tzbD56bxyDGHPuZC3PLD6TvQ5g7gBOYcc4xluxJLyiJG-ygJdf76lhSHxYpb9YXofathQsI4KOszFvPH5ez1w7V0eIe7t8jcA0gZmTSkPkESD0ZQtPvTojyvRHKsqTrX-Ji3Ye7fif-jxq85UlEfo1Qpom9ux2NBX92NYsYb1V98GQPZVdlt2EJ38x7Emj7IRpGB9QfFI5gMCuyzWWBOIoodks3ybk-T1cJ_2CaQgPnqNUA6VqsAUlTBfZIpfgQ3jKAeIfx9Qe0ViCoUSI2x-lLzOeyIuBRzPZNT7ubSKUYK7juAkTYHOACujaaLMx_OiW_GWMxvLJEyYRISxh82VTlVi2DCZ9Sp8tff-3oHB8gLArUroWZ7Do2Tf3ro4XJr6P9PgMtX70V3jM0sp8dJwPmkxvt1NQbL70H_bU1lXo2cR5Q0gE6xMkfmXbqSl0eFOcFU0I2pHETp8EPzlOiQGaZe5xzOqzVK_bC-sYJwhxGC14X9u23Zt24T4BCJdqAZORswsDK0JdY7nNX9QxGadRgM4dF0Gm42lTQcTZlOxkoyX6tiWODu_qLHxbEsQXRHy22ZPI_4UZF-h_nmSMlAcpcRQCYU_JStf_HuzsmqhwTKW3cfdWau0BkOe2uX3FYkOuPTs_sgfeWfT6Igb57rIQGygPNKkEe_oiG4qc1vIjUjynKA=w718-h359-no?authuser=0)
  ![Imagem com Histograma Equalizado](https://lh3.googleusercontent.com/gV-CC4WHhlIRPlIT7ARp9BnTFm9uV8ogqhKct492zenOHUBZ3SqTBKiKIG4kn2SHADRa_UPA3VTRGcokQfa2xvO_4xtP_S3TvZZWav8pOBJEVjp1Q_9pp4Jaf99HfgF3iR77iYl6RXLFlGCrxdUWiy7XHeyXT4nvK3Yd2WTmfk__n5EdHwgO9INmkCdvjj_krIp7-1vOhmTeoKKc0VJiYrXmB_PEi1FBDY_-L21Pm8rkFIK6eBqIqqAcT2KiYiT6oHqu0bOlnoOUTDTw48WkwQ2fJvF2O0JwH5w5793m1IUV4jY6Vkuo63Vbe0xXRO4a3okIelSk0MbP_tq5h1QDYHtkHfufbr0Sgi6ySG5qu5hJvoCoaUCVj7TWzBEXq170bK0MFJGSaPhGQ5XQN9O_V7A6GQae-ODyBjy-QB30Qjej-wkHcoWtGtnlVGXI3rp1-qDeGygex4qh_ssdseOfgFDMR-QtInSr6UOQcGeYJ4pgigMtqZPbA4On8V_OaauY3sSkWc4wM4QPHe3h8tGHFgg1nsoCJAicOEg_n-b8OgWCMht2r9uX7ISVJjyoETUKH53EcHIQZcJ2AYI-61AlnabgHxwxy--Y28nG4ELlfhHSzPJ39mHJAJaxL2wZ9hviUyWW3QpUqWNasLnFFznQqFJoehEgb5NDzaU27YEOe4ksyWdguMDLaVCtexaSfoyxMn26zZXY5ZvSZ8Jz-F9KVrk=w512-h256-no?authuser=0)
  ![Imagem com Histograma Equalizado](https://lh3.googleusercontent.com/c0uGtE7U2-RxuTT3ItelQYw1oK0zHOdrkd4V1C2soqeIc5gmJg-XVly_BwxzLCWuEijmkGDr6jFn6Y7t3f6cKoxKXYe93B0roNOJSwdGsARt_CAcFy6c1HRlO6K0psg8JC_xkEFKxCg5pEVwvRJyZxzv5MV-erO5MsrXT0rCZ8IRi8mRQXv0nuLpWsjt58PQxlEUUnsQi2J-VJWoyK4-VlGFntPusd3dPeE__c1fznK32hy8dAtq1QTt1BqGgnCA6K7_Ku1JNH7jHwaMbYDGOMvFsGeNA-RJrwgP_W4-nLOxr_ValHRqSlPkXfW21tGwl4Kf7ECAssnOr3LKRgcJTuJgfM5Afz5AGShuTdqEpjh0j50C90BL9BpgF5rSg4ffHBTWkbEz40HPDw5u_edqKyckAPuxFKDsqJWVjDwxPEU0np7sedvLQ72RGN1qrBMvYGMCuMGUYArVgHjFKKfvVXxEoyOJmK_dK7MO6Zwm9Pn87uw5o-a3dRxhay4e1yjMK0YEk_EC5OLS-DlmWtJvHEkzADZZLq7SsaI7u0dxSjqnSuf9dHciXZ5OaAggBALf56UkiLRk9nkOUZ3NXAGWbFbGCW7GPK4YsDavVYEgQX838YVNhqZxME-o0l4VHYThKOiVxC6Dqa4JZyJiAGNr2Fb1tFVhRyo37u2dMakd8r-pCK9mTz55EvIFSLhjavqPxlfTZVv8NQKwFAlTkuQpjGA=w1600-h533-no?authuser=0)

## Uso
* Para o funcionamento deste projeto é necessário que as bibliotecas NumPy e OpenCV estejam instaladas. Instale utilizando os comandos:
  * `pip3 install NumPy`
  * `pip3 install opencv-python`
* Há sugestões de imagens para testes na pasta `sample`.
* As imagens resultantes do programa são salvas na pasta `export`.

## Tecnologias utilizadas
* Python 3.9.3
  * OpenCV 4.5.2.52
  * NumPy 1.20.2

## Documentação
* [OpenCV Docs](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
* [NumPy Docs](https://numpy.org/doc/)

