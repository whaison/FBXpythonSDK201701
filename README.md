# FBXpythonSDK201701
Unofficial FBXpythonSDK201701

  | http://usa.autodesk.com/adsk/servlet/pc/item?siteID=123112&id=26012646 
  |  http://download.autodesk.com/us/fbx/2017/2017.1/fbx20171_fbxpythonsdk_win.exe

  
  
  
  
  
http://www.graphviz.org/Download_windows.php

http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-2.38.msi


http://effbot.org/downloads#elementtree

http://effbot.org/media/downloads/elementtree-1.2.6-20050316.tar.gz





URL
python doxygenで、各種形式のドキュメントを作ってしまおう 00:20

http://d.hatena.ne.jp/Wacky/20051023/1130080826

C/C++だと、doxygen
Javaだと、JavaDoc
Pythonだと、pydoc
あたりが有名みたいだ。


Step1
working directory	dokigen
   doxygenに喰わせてドキュメント化したファイル群を置く場所を示す。

Project name	
   タイトル名みたいなもの。ここでは、"ElementTree(doxygen)"とした
Source code directory	
   doxygenに喰わせるソースの在り処を示す。
    サブディレクトリにもある場合、"Scan recursively"にチェックを入れれば良いと思う

	
	
	-----------------------
	mode
	
	Select the desired extraction mode	
	  多分、ドキュメント化の範囲。
      ここでは、"Document entities only"にしてある。"All entities"とか"Include cross-referenced source code in the output"にチェックを入れると、ドキュメントに より多くのソース情報を含ませるハズ
   Select programming language to optimize the result for
      ソースに書き込んだドキュメント形式を教えろと言っているハズ。
      ここでは、"Optimize for Java Output"としているのは、
	  Special documentation blocks in Pythonここに設定ファイルに、
	  "OPTIMIZE_OUTPUT_JAVA"って設定しろとあったから
	  
	  
	  
	  -------------------------------
	  
	  Outputタブは、出力するドキュメントの種類を指定する。

    ここでは、以下のようにしてみた。

    HTML	チェック入れるとHTMLファイルを出力する。
	      ここでは、閲覧性に優れる HTML Help形式(.chm)が欲しかったので、"prepare for compressed HTML"を選んだ
    Man pages	Unixで有名な man 形式ね
    Rich Text Format(RTF)	Wordで読み取れる形式ね
    XML	XMLファイル形式ね
	
	
	-------------------------------------
	
	
    Diagramsタブは、クラス構造を図化する種類を指定する。

     ここでは、以下のようにしてみた。

      Diagrams to generate	
	            ここでは、上で折角 Graphviz 入れたので、"Use dot tool from the Graphviz package to generate"を選んでみた。
             図なんか要らねぇって場合は、"No diagrams"とか選べばOKのハズ


	---------------------------------------------
	
	=============================================
	https://github.com/whaison/doxypypy
	
	Using c:\python27\lib\site-packages
Processing dependencies for doxypypy
Finished processing dependencies for doxypypy

C:\Python27>pip install doxypypy
Requirement already satisfied: doxypypy in c:\python27\lib\site-packages

C:\Python27>doxypypy -a -c file.py > file.py.out

	=================================================
	Doxygenからのdoxypypyの呼び出し
    ==================
    DoxygenをdoxypypyでPythonコードを実行させるには、FILTER _PATTERNSを設定します タグをDoxyfileに追加します。

FILTER_PATTERNS        = *.py=py_filter

`py_filter`はあなたのパスでシェルスクリプト（またはWindowsバッチ）として利用可能でなければなりません ファイル）。特定のディレクトリで `py_filter`を実行したい場合は、 完全パスまたは相対パス。

doxypypy -a -c %1

いつものようにDoxygenを実行すると、すべてのPythonコードがdoxypypyで実行されるはずです。 
Be Doxygenの出力を最初に慎重に閲覧してください Doxygenは適切に見つけられ、doxypypyを実行しました。

