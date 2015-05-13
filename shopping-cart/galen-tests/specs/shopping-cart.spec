=====================================
header          css #header
navigation      css #navigation
main            css #main-container
banner-panel    css #banner-panel
footer          css #footer
=====================================

@ Header | *
--------------------
header
  inside: screen 0px top left right
  height: 58px

@ Navigation | *
-------------------
navigation
  inside: screen 0px left
  below: header 0px

@^| desktop
-----------------------
navigation
  width: 185 to 335px
  aligned horizontally all: main
  near: main 0px left

@^| tablet
-----------------
navigation
  inside: screen 0px left right
  above: main 0px
  % height: 50 to 100px

@^| mobile
----------------------
navigation
  inside: screen 0px left right
  above: main 0px
  % height: > 60px

@ Footer | *
-------------------
footer
  % inside: screen 0px left right
  below: banner-panel 0px
  height: 100px

@ Main | desktop
-----------------------
main, banner-panel
  below: header 0px

@^| tablet
----------
main
  inside: screen 0px left
  below: navigation 0px

@^| mobile
------------------
main
  inside: screen 0px left right
  above: banner-panel 0px

@ Banner panel | desktop, tablet
-------------------
banner-panel
  width: 220 to 400px
  aligned horizontally all: main

@^| tablet
--------------------
banner-panel
  below: navigation 0px

@^| mobile
------------------
banner-panel
  inside: screen 0px left right
  % height: > 50px