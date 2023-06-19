import uuid

data = [
["CC0603JRNPO9BN270","C107045","B","50V","27pF","NP0","±5%","0603","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/1811082127_YAGEO-CC0603JRNPO9BN270_C107045.pdf","190804","0.003$/unit0.003$/1 units"],
["1206B103K500NT","C1846","B","50V","10nF","X7R","±10%","1206","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-1206B103K500NT_C1846.pdf","255742","0.012$/unit","0.012$/1 units"],
["1206B224K500NT","C1857","B","50V","220nF","X7R","±10%","1206","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-1206B224K500NT_C1857.pdf","60958","0.027$/unit","0.027$/1 units"],
["1206B475K500NT","C29823","B","50V","4.7uF","X7R","±10%","1206","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-1206B475K500NT_C29823.pdf","325157","0.032$/unit","0.032$/1 units"],
["1206B102K202NT","C9196","B","2kV","1nF","X7R","±10%","1206","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-1206B102K202NT_C9196.pdf","1044247","0.005$/unit","0.005$/1 units"],
["CL31A226KAHNNNE","C12891","B","25V","22uF","X5R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31A226KAHNNNE_C12891.pdf","4405590","0.046$/unit","0.046$/1 units"],
["CL31A106KBHNNNE","C13585","B","50V","10uF","X5R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31A106KBHNNNE_C13585.pdf","1415543","0.03$/unit","0.03$/1 units"],
["CL31A107MQHNNNE","C15008","B","6.3V","100uF","X5R","±20%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31A107MQHNNNE_C15008.pdf","311539","0.058$/unit","0.058$/1 units"],
["CL31B105KBHNNNE","C1848","B","50V","1uF","X7R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31B105KBHNNNE_C1848.pdf","2018777","0.027$/unit","0.027$/1 units"],
["CL31B104KBCNNNC","C24497","B","50V","100nF","X7R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31B104KBCNNNC_C24497.pdf","379300","0.013$/unit","0.013$/1 units"],
["CL31B102KGFNNNE","C35216","B","500V","1nF","X7R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31B102KGFNNNE_C35216.pdf","26737","0.03$/unit","0.03$/1 units"],
["CL31B225KBHNNNE","C50254","B","50V","2.2uF","X7R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31B225KBHNNNE_C50254.pdf","181214","0.031$/unit","0.031$/1 units"],
["CL31A226KPHNNNE","C5672","B","10V","22uF","X5R","±10%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810221121_Samsung-Electro-Mechanics-CL31A226KPHNNNE_C5672.pdf","156570","0.024$/unit","0.024$/1 units"],
["CL31A476MPHNNNE","C96123","B","10V","47uF","X5R","±20%","1206","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL31A476MPHNNNE_C96123.pdf","169129","0.075$/unit","0.075$/1 units"]

]

print ("""
(lib_symbols
  (symbol "Device:C_Small" (pin_numbers hide) (pin_names (offset 0.254) hide) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 0.254 1.778 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "C_Small" (at 0.254 -2.032 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "~" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "capacitor cap" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "Unpolarized capacitor, small symbol" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_fp_filters" "C_*" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "C_Small_0_1"
      (polyline
        (pts
          (xy -1.524 -0.508)
          (xy 1.524 -0.508)
        )
        (stroke (width 0.3302) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.524 0.508)
          (xy 1.524 0.508)
        )
        (stroke (width 0.3048) (type default))
        (fill (type none))
      )
    )
    (symbol "C_Small_1_1"
      (pin passive line (at 0 2.54 270) (length 2.032)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -2.54 90) (length 2.032)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
)""")

#0 "CL10A105KB8NNNC"
#1 "C15849"
#2 "B"
#3 "50V"
#4 "1uF"
#5 "X5R"
#6 "±10%"
#7 "0603"
#8 "SMD/SMT"
#9 "ROHS"
#10 "Samsung Electro-Mechanics"
#11 "https://datasheet.lcsc.com/lcsc/1810261812_Samsung-Electro-Mechanics-CL10A105KB8NNNC_C15849.pdf"
#12 "5349163"
#13 "0.005$/unit0.005$/1 units"]


#0 "CL05A105KA5NQNC"
#1 "C52923"
#2 "B"
#3 "25V"
#4 "1uF"
#5 "X5R"
#6 "±10%"
#7 "0402"
#8 "SMD/SMT"
#9 "ROHS"
#10 "Samsung Electro-Mechanics"
#11 "https://datasheet.lcsc.com/lcsc/1811091611_Samsung-Electro-Mechanics-CL05A105KA5NQNC_C52923.pdf"

# "1206B103K500NT",
# "C1846",
# "B",
# "50V",
# "10nF",
# "X7R",
# "±10%",
# "1206",
# "SMD/SMT",
# "ROHS",
# "FH (Guangdong Fenghua Advanced Tech)",
# "https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-1206B103K500NT_C1846.pdf",
# "255742",
# "0.012$/unit",
# "0.012$/1 units"








n = 0
v1 = 60.96
v2 = 38.1
v3 = 63.5
v4 = 35.56
v5 = 69.85
v6 = 40.64
v7 = 57.15
v8 = 54.61
step = 5.08
for x in data:

    v1 += step
    v2 += step
    v3 += step
    v4 += step
    v5 += step
    v6 += step
    v7 += step
    v8 += step
    #print(x)
    #print(num)
    #num+=1
    #(uuid """ + str(uuid.uuid4()) + """)
    print ("""
(symbol (lib_id "Device:C_Small") (at """ + str(v1) + """ """ + str(v2) + """ 90) (unit 1)
  (in_bom yes) (on_board yes) (dnp no)

  (property "Reference" "C" (at """ + str(v8) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Value" """ + '"' + x[4] + '"' + """ (at """ + str(v3) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Datasheet" """ + '"' + x[11] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "LCSC" """ + '"' + x[1] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Manufacturer Part" """ + '"' + x[0] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Tolerance" """ + '"' + x[6] + '"' + """ (at """ + str(v3) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Voltage Rated" """ + '"' + x[3] + '"' + """ (at """ + str(v5) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Dielectric" """ + '"' + x[5] + '"' + """ (at """ + str(v3) + """ """ + str(v6) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Manufacturer" """ + '"' + x[10] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Supplier Footprint" """ + '"' + x[7] + '"' + """ (at """ + str(v7) + """ """ + str(v6) + """ 90)
    (effects (font (size 1.27 1.27)))
  )
  (pin "1" (uuid """ + str(uuid.uuid4()) + """))
  (pin "2" (uuid """ + str(uuid.uuid4()) + """))
)
""")
