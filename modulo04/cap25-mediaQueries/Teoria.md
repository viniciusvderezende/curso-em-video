# Media Queries

Traduzido do inglês - As consultas de mídia são um recurso do CSS 3 que permite que a renderização do conteúdo se adapte a diferentes condições, como a resolução da tela. Tornou-se um padrão recomendado pelo W3C em junho de 2012, e é uma tecnologia fundamental de web design responsivo. Fonte: <a href="https://en.wikipedia.org/wiki/Media_queries" target="_blank">Wikipedia.</a>  
Correspondem à junção de media types e media features.

### Media Types

São os tipos de mídia para as quais estamos gerando estilização.  
Em HTML, temos media="screen" (para telas) e media="print" (para impressão).  
Esses dois atributos são inseridos ao final da tag link de CSS. Ex.:  

<code>
    link rel="stylesheet" href="estilos/tela.css" media="screen"
</code><br>
<code>
    link rel="stylesheet" href="estilos/impressora.css" media="print"
</code>
<code>
    link rel="stylesheet" href="estilos/impressora.css" media="all"
</code>

O tipo media="all", serve para todos os tipos de exibições.

### Configurando estilo para impressão

Nas CSS's abaixo, resetamos as configurações de margem e preenchimento dos elementos.  
Na seqência, definimos os padrões para a fonte do conteúdo.  
Como esse estilo foi criado para impressões, retiramos o menu que é exibido nas telas através da classe menu - display: none.  
Em article, configuramos a impressão para a totalidade do espaço de impressão e uma mensagem a ser exibida ao final do artigo quando a página for impressa.

<code>
    * {
        margin: 10px;  
        padding: 10px;      
    }  
    
    html {
        font-family: 'Courier New', Courier, monospace;
        font-size: 1em;
        line-height: 1.5em;
    }

    menu {
        display: none;
    }

    article {
    width: 100%;
    }

    article::after {
    content: 'Esse artigo foi impresso através do site www.cursoemvideo.com';
    }
</code>

### Configurando estilo para telas

Nas CSS's que seguem, temos a configuração de padrão de exibição do conteúdo em html, a cor do fundo do header, o alinhamento do texto do título, a estilização e cor do menu, formatamos cada item do menu em "menu li". Para que os itens fossem posicionados lado a lado, precisamo configurar o display como inline-block (bloco em linha), demos um preenchimento em cada item com padding, configuramos o espaço que o artigo ocupará na tela e, para **centralizá-lo**, precisamos configurar o **display** como **block** e a **margem, automática**.

<code>
    * {
    margin: 0px;
    padding: 0px;    
    }

    html {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1em;
    }

    header {
        background-color: lightgrey;
    }

    header > h1 {
        text-align: center;
    }

    menu ul {
        list-style-type: none;
        background-color: grey;
    }

    menu li {
        background-color: rgb(80, 80, 80);
        color: white;
        display: inline-block;
        padding: 10px;
    }

    article {
        width: 600px;
        display: block;
        margin: auto;
    }
</code>

### Media Features

São as características das diversas mídias ou telas onde o conteúdo será exibido.

<quote>
    "Um media feature é a largura da janela do documento, normalmente usado para atribuir uma condição que vai testar se o que foi definido é verdadeiro ou falso, ou seja, são elementos do CSS atribuídos a estrutura do media para exibir quando a estilização sofrerá modificação".
</quote>

Fonte: <a href="https://www.treinaweb.com.br/blog/media-queries-o-que-sao-e-como-usar-no-css#:~:text=Um%20media%20feature%20%C3%A9%20a,quando%20a%20estiliza%C3%A7%C3%A3o%20sofrer%C3%A1%20modifica%C3%A7%C3%A3o." target="_blank">Treinaweb.</a>  

As media features são inseridas ao final do link das CSS's no deader do HTML, porém, são diferentes das media types, pois são declaradas entre parênteses como no modelo abaixo:  

<code>
    link rel="stylesheet" href="estilos/style.css" media="all"
    link rel="stylesheet" href="estilos/retrato.css" media="screen and (orientation: portrait)"
    link rel="stylesheet" href="estilos/paisagem.css" media="screen and (orientation: landscape)"
</code>

Nesse caso, determinamos a media feature de orientação de tela para exibição do conteúdo **(landscape = paisagem e portrait = retrato)**.