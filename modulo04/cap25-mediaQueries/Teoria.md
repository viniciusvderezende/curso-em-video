# Media Queries

Traduzido do inglês - As consultas de mídia são um recurso do CSS 3 que permite que a renderização do conteúdo se adapte a diferentes condições, como a resolução da tela. Tornou-se um padrão recomendado pelo W3C em junho de 2012, e é uma tecnologia fundamental de web design responsivo. Fonte: <a href="https://en.wikipedia.org/wiki/Media_queries">Wikipedia.</a>  

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