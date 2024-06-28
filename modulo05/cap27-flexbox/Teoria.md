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

## Direções e eixos em flexbox

### Flex-direction

A propriedade flex-direction receberá alguns atributos para a orientação do posicionamento dos elementos-filho, pois flex direction será declarado no elemento-pai. São esses atributos:

- row;
- row-reverse.
- column.
- column-revere.

#### Row:

A configuração padrão do flex-direction é row, portanto, se não declararmos nada, o conteúdo permanecerá em linha, orietado da esquerda para direita.

#### Curiosidade
Nas linguas em que o sentido da leitura é da direita para esquerda, como o árabe, por exemplo, o flex-direction será da direita para a esquerda.

#### Row-reverse: 
Podemos declarar o sentido inverso do flex-direction row. Para isso, utilizaremos a propriedade row-reverse. Dessa forma, a orientação será da direita para a esquerda.

#### Column: 

Para posicionarmos os itens em formato vertical, utilizaremos a propriedade column.

#### Column-reverse:

Tal qual a o atributo row reverse, o column-reverse posicionará os itens na vertical, orientados de baixo para cima.

### Eixos (axis)

A orientação do conteúdo é disposta na horizontal ou na vertical é composta pelos eixos X e Y, sendo o eixo X o orientador da horizontal e, o eixo Y, da vertical.

Ao iniciarmos a propriedade flex-direction: row, criaremos o eixo principal (main-axis) que é o eixo horizontal. Todo eixo é composto por dois pontos: o inicial (main-start) e o final (main-end), da esquerda para direita.
O outro eixo criado é o eixo vertical, o cross-axis, que também é composto pelo cross-start e cross-end, de cima para baixo.

Vale ressaltar que, quando o atributo for acompanhado do reverse, o start e end também se invertem. Ex.:

row-reverse: o start para a partir da direita.

Se declararmos o flex-direction como column, teremos o main-axis de cima para baixo e o cross-axis, da esquerda para a direita. Seguimos o mesmo padrão relatado no row-reverse se declararmos o column-reverse.

Em todos os casos, quando novos itens forem adicionados ou deslocados, isso ocorrerá do start para o end.

### Flex-wrap

O padrão da propriedade é nowrap, ou seja, não vai deslocar o conteúdo quando houver a diminuição do elemento-pai.  
Assim, reduzindo a tela, o conteúdo será reduzido, ou "espremido".  
Vale ressaltar que, o tamanho do bloco, dependerá do conteúdo exitente nele.  
Ao inserirmos flex-wrap no elemento-pai, os elementos filhos já estarão configurados como now-rap, não havendo necessidade de declarar esse atributo nos elementos-filho.

#### Wrap:  

Essa propriedade desloca o último elemento-filho no cross-axis, ou seja, no eixo transversal. Se a direction estiver como padrão (da esquerda para a direita), o último elemento será direcionado para baixo, quando o elemento pai for reduzido.

#### Wrap-reverse:

Quando o conteúdo for reduzido, o último elemento será deslocado no sentido oposto do cross-axis, ou seja, será deslocado para cima, se a direction estiver padrão.

