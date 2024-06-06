# Flexbox

## Questionamentos interessantes da aula:

- ### Qual é o formato da água?
    - A água não tem formato definido.
    - Seu formato depende do recipiente onde ela está contida.
      - Nomeamos o recipiente como "contêiner".
    - Se diminuirmos o recipiente sem reduzir a água, ela transbordará.

Da mesma maneira que a água se comporta, o flexbox permite moldar toda a estrutura de layout de forma fluida e mais assertiva.  
Entendemos o recipeinte da água como sendo os conêineres e, a água por sua vez, representa todo o conteúdo existente nos contêineres, que tomarão forma de acordo com o que parametrizarmos para os contêineres. Tal qual a água transborda se reduzirmos o tamanaho do seu recipiente, o conteúdo dos contêineres não se ajustam sem que haja configuração adequada para isso.
Isso permite trabalhar com mais assertividade as questões de responsividade e tornar o layout mais facilmente adaptável aos diversos tipos de dispositivos.

- ### Quem é o pai?

É justamente o contêiner!  
Más, para existir um pai, é necessária a existência dos filhos, certo?  
Sim! Os filhos são justamente a água, ou todo o conteúdo do contêiner!  
Dessa forma, os elementos filho serão deslocados ou moldados de acordo com o tipo de display que determinarmos para o elemento pai. No caso do assunto que estamos tratando, o display flex.  
É importante salientar que, apenas o elemento pai recebe a configuração de display flex. Os elementos filho receberão outras configurações.

Denominamos os elementos pai como _**flex-contêiner** e os elementos filho, chamamos de _**flex-items**_._