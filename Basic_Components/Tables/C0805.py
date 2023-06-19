import uuid

data = [
["CC0805JRNPO9BN150","C107110","B","50V","15pF ","NP0 ","±5%","0805","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2304140030_YAGEO-CC0805JRNPO9BN150_C107110.pdf","31725","0.006$/unit 0.006$/1 units"],
["CC0805JRNPO9BN300","C107114","B","50V","30pF ","NP0 ","±5%","0805","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2304140030_YAGEO-CC0805JRNPO9BN300_C107114.pdf","114049","0.006$/unit 0.006$/1 units"],
["CC0805JRNPO9BN330","C107115","B","50V","33pF ","NP0 ","±5%","0805","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2304140030_YAGEO-CC0805JRNPO9BN330_C107115.pdf","87275","0.006$/unit 0.006$/1 units"],
["CC0805KRX7R9BB221","C107145","B","50V","220pF ","X7R","±10%","0805","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2304140030_YAGEO-CC0805KRX7R9BB221_C107145.pdf","115042","0.005$/unit 0.005$/1 units"],
["CL21B474KBFNNNE","C13967","B","50V","470nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B474KBFNNNE_C13967.pdf","226409","0.013$/unit 0.013$/1 units"],
["CL21C470JBANNNC","C14857","B","50V","47pF ","C0G","±5%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21C470JBANNNC_C14857.pdf","82468","0.012$/unit 0.012$/1 units"],
["CL21A106KAYNNNE","C15850","B","25V","10uF ","X5R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21A106KAYNNNE_C15850.pdf","2710730","0.011$/unit 0.011$/1 units"],
["CL21A476MQYNNNE","C16780","B","6.3V","47uF ","X5R","±20%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21A476MQYNNNE_C16780.pdf","937463","0.021$/unit 0.021$/1 units"],
["CL21B103KBANNNC","C1710","B","50V","10nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B103KBANNNC_C1710.pdf","363475","0.009$/unit 0.009$/1 units"],
["0805B151K500NT","C1716","B","50V","150pF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B151K500NT_C1716.pdf","51216","0.005$/unit 0.005$/1 units"],
["0805B152K500NT","C1717","B","50V","1.5nF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B152K500NT_C1717.pdf","67730","0.004$/unit 0.004$/1 units"],
["CL21B223KBANNNC","C1729","B","50V","22nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B223KBANNNC_C1729.pdf","96094","0.009$/unit 0.009$/1 units"],
["0805B333K500NT","C1739","B","50V","33nF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B333K500NT_C1739.pdf","86426","0.007$/unit 0.007$/1 units"],
["0805B334K500NT","C1740","B","50V","330nF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B334K500NT_C1740.pdf","47407","0.012$/unit 0.012$/1 units"],
["0805B471K500NT","C1743","B","50V","470pF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B471K500NT_C1743.pdf","107832","0.004$/unit 0.004$/1 units"],
["0805B472K500NT","C1744","B","50V","4.7nF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B472K500NT_C1744.pdf","139132","0.004$/unit 0.004$/1 units"],
["0805B682K500NT","C1755","B","50V","6.8nF ","X7R","±10%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805B682K500NT_C1755.pdf","35308","0.004$/unit 0.004$/1 units"],
["CL21A475KAQNNNE","C1779","B","25V","4.7uF ","X5R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21A475KAQNNNE_C1779.pdf","1624073","0.011$/unit 0.011$/1 units"],
["CL21C101JBANNNC","C1790","B","50V","100pF ","C0G","±5%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21C101JBANNNC_C1790.pdf","251101","0.009$/unit 0.009$/1 units"],
["0805CG120J500NT","C1792","B","50V","12pF ","C0G","±5%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805CG120J500NT_C1792.pdf","30402","0.005$/unit 0.005$/1 units"],
["0805CG180J500NT","C1797","B","50V","18pF ","C0G","±5%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805CG180J500NT_C1797.pdf","48962","0.005$/unit 0.005$/1 units"],
["CL21C200JBANNNC","C1798","B","50V","20pF ","C0G","±5%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21C200JBANNNC_C1798.pdf","89770","0.013$/unit 0.013$/1 units"],
["CL21C220JBANNNC","C1804","B","50V","22pF ","C0G","±5%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21C220JBANNNC_C1804.pdf","369360","0.011$/unit 0.011$/1 units"],
["CL21B104KCFNNNE","C28233","B","100V","100nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B104KCFNNNE_C28233.pdf","331011","0.007$/unit 0.007$/1 units"],
["CL21C222JBFNNNE","C28260","B","50V","2.2nF ","C0G","±5%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21C222JBFNNNE_C28260.pdf","54448","0.033$/unit 0.033$/1 units"],
["CL21B105KBFNNNE","C28323","B","50V","1uF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B105KBFNNNE_C28323.pdf","1823301","0.009$/unit 0.009$/1 units"],
["GRM21BR61H106KE43L","C440198","B","50V","10uF ","X5R","±10%","0805","SMD/SMT","ROHS","Murata Electronics","https://datasheet.lcsc.com/lcsc/2004251506_Murata-Electronics-GRM21BR61H106KE43L_C440198.pdf","378572","0.074$/unit 0.074$/1 units"],
["CL21A226MAQNNNE","C45783","B","25V","22uF ","X5R","±20%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21A226MAQNNNE_C45783.pdf","601770","0.024$/unit 0.024$/1 units"],
["CL21B102KBCNNNC","C46653","B","50V","1nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B102KBCNNNC_C46653.pdf","198247","0.011$/unit 0.011$/1 units"],
["0805F225M500NT","C49217","B","50V","2.2uF ","Y5V","±20%","0805","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2304140030_FH--Guangdong-Fenghua-Advanced-Tech-0805F225M500NT_C49217.pdf","286810","0.016$/unit 0.016$/1 units"],
["CC0805KRX7R9BB104","C49678","B","50V","100nF ","X7R","±10%","0805","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2304140030_YAGEO-CC0805KRX7R9BB104_C49678.pdf","10781848","0.004$/unit 0.004$/1 units"],
["CL21B473KBCNNNC","C53134","B","50V","47nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B473KBCNNNC_C53134.pdf","89871","0.011$/unit 0.011$/1 units"],
["CL21B224KBFNNNE","C5378","B","50V","220nF ","X7R","±10%","0805","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B224KBFNNNE_C5378.pdf","136292","0.011$/unit 0.011$/1 units"]
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

#0 "CL21B224KBFNNNE"
#1 "C5378"
#2 "B"
#3 "50V "
#4 "220nF "
#5 "X7R"
#6 "±10%"
#7 "0805"
#8 "SMD/SMT "
#9 "ROHS"
#10 "Samsung Electro-Mechanics"
#11 "https://datasheet.lcsc.com/lcsc/2304140030_Samsung-Electro-Mechanics-CL21B224KBFNNNE_C5378.pdf"





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
