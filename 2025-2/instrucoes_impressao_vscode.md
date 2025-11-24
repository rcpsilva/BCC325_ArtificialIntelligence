# 🖨️ Como imprimir um arquivo `.py` com **linhas numeradas** no VS Code

Este guia utiliza a extensão **Print (pdconsec.vscode-print)**, que está atualizada e permite imprimir código com numeração de linhas.

---

## 1. Abrir o arquivo `.py`
1. Abra o **VS Code**.  
2. Vá em **File → Open File…** e selecione o arquivo que deseja imprimir.

---

## 2. Ativar numeração de linhas no editor (opcional)
Embora a extensão permita controlar isso, é útil visualizar enquanto edita.

1. Clique no ícone de **engrenagem** (canto inferior esquerdo).  
2. Selecione **Settings**.  
3. Busque por: `line numbers`.  
4. Em **Editor: Line Numbers**, escolha **on**.

---

## 3. Instalar a extensão *Print*
1. Abra o painel de extensões (`Ctrl + Shift + X`).  
2. Busque por:  
   ```
   Print
   ```  
3. Instale a extensão **Print – pdconsec.vscode-print**.

---

## 4. Configurar a extensão para exibir linhas numeradas
1. Vá em **Settings**.  
2. Busque por:
   ```
   print
   ```  
3. Localize as configurações da extensão **Print**.  
4. Ative (ou confirme ativado):  
   - **Line Numbers** → `true`

---

## 5. Gerar a visualização para impressão
1. Abra a paleta de comandos com:  
   ```
   Ctrl + Shift + P
   ```  
2. Digite:
   ```
   Print: Print
   ```
3. A extensão abrirá uma **visualização HTML no navegador** contendo:  
   - o código formatado  
   - linhas numeradas  
   - sintaxe colorida  

---

## 6. Imprimir ou salvar em PDF
1. No navegador, pressione **Ctrl + P**.  
2. Ajuste:
   - **Destination** → Impressora ou *Save as PDF*  
   - **Margins**  
   - **Layout** (portrait/landscape)  
   - Desative cabeçalhos/rodapés, se desejar  
3. Clique em **Print**.

---

## ✔️ Concluído!
Seu arquivo `.py` será imprenso com **numeração de linhas**, formatação correta e destaque de sintaxe.
