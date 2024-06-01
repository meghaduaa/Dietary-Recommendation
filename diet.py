import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my webpages", page_icon=":tada:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

# Use local CSS

#--assets load-
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_nq22pa14.json")

#---HEADER---
with st.container():
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.title("Diet recomendations")
        st.subheader(":red[About us]")
        st.write("We aim at providing customized dietary recommendations and opinions for people with different age , health conditions and body types.")
        st.write("The recommendations and opinions provided as a result are backed by inputs provided by dietitians.")
        st.write("We further aim at providing better alternatives for the user’s selected food items and also provide them with a personalized dietary plan which suits their body.")
        
    with right_coloumn:
        st_lottie(lottie_coding , height=300, key="recommendations")



#---some content--
with st.container():
    st.write("---")
    st.subheader("**How does it works :interrobang:**")
    st.write("""-Users are given a list of factors, each of which consists different body traits. The user is supposed to select the trait that suits their body type the most.\n
-User Inputs, specifically , BMI(Body Mass Index), any pre-existing health condition (Diabetes,PCOD, abnormal Blood Pressure), Dietary preferences are taken which therby determine the suitability of the food item for that user.\n
-The user input is then processed and appropriate personalized food options are suggested.\n

The users choice is also taken into consideration and opinions are suggested accordingly""")



st.write("---")

oglst=["Salt","Chicken/Meat","Fish","Rice","Wheat","Sugar","Egg","Fruits","Milk"]
st.subheader("Choose your Dietary preferences")
res= st.selectbox("Select",oglst)
st.write("##")
st.write("##")


oglt=["","Abnormal Blood Pressure","Diabetes","PCOD","Dengue","Jaundice"]
st.subheader("Choose your Disease")
rs= st.selectbox("Select",oglt)
st.write("##")
st.write("##")


ogl=["","Underweight(less than 18.5)","Normal(18.5 to 25)","Overweight(25 to 30)","Obese(more than 30)"]
st.subheader("Choose your BMI Categorgy")
st.write("[Calculate your BMI here >](https://www.calculator.net/bmi-calculator.html)")
ras= st.selectbox("Select",ogl)

st.write("##")
st.write("##")
m=st.button("Confirm")
if m:
    if res=="Rice":
        if rs=="Thyroid":
            if ras=="Overweight(25 to 30)" or ras=="Obese(more than 30)":
                st.subheader(":red[No, rice may lead to weight gain if it is eaten with a less nutritious diet, but it can help contribute to weight management if eaten as part of a well-balanced diet]")
                st.write("##")
                st.subheader(":green[Rather than you can go for more complex carbohydrates]")

            elif ras=="Normal(18.5 to 25)":
                st.subheader(":red[No, rice may lead to weight gain if it is eaten with a less nutritious diet, but it can help contribute to weight management if eaten as part of a well-balanced diet]")
                st.write("##")
                st.subheader(":green[Whole Grains Try to eat oats, brown rice, sprouts, sprouted grain bread and quinoa to rev up your metabolism and help your thyroid gland.]")

            elif ras=="Underweight(less than 18.5)":
                st.subheader(":green[Yes you may,because Consumption of Rice during thyroid being an underweight person ]")
            
            else:
                st.subheader(":orange[Yes you may,You haven't selected any of the BMI Categories ]")
        
        elif rs=="Abnormal Blood Pressure":
            if ras=="Overweight(25 to 30)" or ras=="Obese(more than 30)":
                st.subheader(":red[No, rice may lead to collection of Triglycerids being accumulated on the walls of heart,if rice is being consumed during Abnormal blood pressure of an above average weight then it could lead to stroke as well]")
                st.write("##")
                st.subheader(":green[White rice is high in carbohydrates and low in nutrients that help control your blood pressure. Therefore, it is better to choose brown rice in place of white rice in order to maintain healthy blood pressure levels.]")
            
            elif ras=="Normal(18.5 to 25)":
                st.subheader(":red[No, rice may lead to weight gain if it is eaten with a less nutritious diet, but it can help contribute to weight management if eaten as part of a well-balanced diet]")
                st.write("##")
                st.subheader(":green[Whole Grains Try to eat oats, brown rice, sprouts, sprouted grain bread and quinoa to rev up your metabolism and help your thyroid gland.]")

            elif ras=="Underweight(less than 18.5)":
                st.subheader(":green[Yes you may,because Consumption of Rice during abnormal blood pressure being an underweight person]")
            
            else:
                st.subheader(":orange[Yes you may,You haven't selected any of the BMI Categories ]")
        
        elif rs =="Diabetes":
                if ras=="Overweight(25 to 30)" or ras=="Obese(more than 30)":
                  st.subheader(":red[No, rice may lead to collection of Triglycerids being accumulated on the walls of heart,if rice is being consumed during Abnormal blood pressure of an above average weight then it could lead to stroke as well]")
                  st.write("##")
                  st.subheader(":green[brown rice is high in carbohydrates and low in nutrients that help control your diabetes. Therefore, it is better to choose brown rice in place of white rice in order to maintain healthy blood pressure levels.]")

                elif ras=="Normal(18.5 to 25)":
                  st.subheader("White rice has a high glycemic index, meaning that it can cause spikes in blood sugar. Previous research has linked high glycemic index foods with increased type 2 diabetes risk")
                  st.write("##")
                  st.subheader(":green[Consumption of rice for a normal guy mustn't neededly include rice being a type 1 or type 2 diabetic ]")

                elif ras=="Underweight(less than 18.5)":
                  st.subheader(":green[Yes you may,because Consumption of Rice during Type 1 or type 2  diabetes 5being an underweight person]")
            
                else:
                  st.subheader(":orange[Yes you may,You haven't selected any of the BMI Categories ]")
                
    
    elif res=="Sugar":
        if rs == "PCOD":
            st.subheader(":red[No,it is critical to avoid high sugar foods with PCOS. Eating less sugar results in lower blood glucose levels. This decreases insulin levels, and reduces male hormone levels. ]")
            st.write("##")
            st.subheader(":green[Adding high quality fat to your meal can actually aid digestion and slow the release of glucose from carbohydrates into your body ]")
        elif rs == "Diabetes":
            st.subheader(":green[You don't need to cut out sugar from your diet if you have diabetes.You just need to Limit the intake of free sugars to less than 10 percent of total daily calorie (energy) intake.]")
            st.write("##")
        elif rs == "Jaundice" or rs=="Dengue"   :
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)":
                st.subheader(":red[It may be possible that you will have to limit higher intakes of sugar as your liver heals and also sugar contributes to weight gain]")
                st.write("##")
                st.subheader(":green[Try going for alternatives of sugar such as jaggery] ")
            else :
                st.subheader(":red[It may be possible that you will have to limit higher intakes of sugar as your liver heals]")
                st.write("##")
                st.subheader(":green[Try going for alternatives of sugar such as jaggery] ")


        elif rs=="Abnormal Blood Pressure":
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)":
                st.subheader(":red[Foods high in salt, sugar, and saturated or trans fats can increase blood pressure and damage your heart health.]")
                st.write("##")
                st.subheader(":green[By limiting these foods and replacing them with healthy options, you can keep your blood pressure at a healthy level.]")
            else:
                st.subheader(":red[Foods high in salt, sugar, and saturated or trans fats can increase blood pressure and damage your heart health.]")
                st.write("##")
                st.subheader(":green[By limiting these foods and replacing them with healthy options, you can keep your blood pressure at a healthy level.]")
        else:
                st.subheader(":orange[Yes you may have it]")
    elif res == "Egg":
        if rs == "Diabetes":
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)":
                st.subheader(":green[Yes,Protein-rich foods like eggs can play an important role in regulating blood sugar levels for people with diabetes. Plus, eggs contain many essential vitamins and minerals, and have just 80 calories each.]")
                st.write("##")
            else :
                st.subheader(":green[Yes,Protein-rich foods like eggs can play an important role in regulating blood sugar levels for people with diabetes. Plus, eggs contain many essential vitamins and minerals, and have 80 calories each.]")
                st.write("##")
        elif rs == "PCOD":
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)":
                st.subheader(":green[Yes,Eggs are great for women with PCOS trying to lose weight. They are full of protein that helps curb unhealthy cravings and have nutrients that improve PCOD symptoms.]")
                st.write("##")
            elif ras == "Underweight(less than 18.5)" :
                st.subheader(":green[Yes,Eggs are great for women with PCOS.They are full of protein that helps curb unhealthy cravings and have nutrients that improve PCOD symptoms.They can be consumed with add-ons like cheese to increase the calorie content]")
                st.write("##")
            else :
                st.subheader(":green[Yes,Eggs are great for women with PCOS.They are full of protien that helps curb unhealthy cravings and have nutrients that improve PCOD symptoms.]")
                st.write("##")
        elif rs == "Dengue" or "Jaundice" :
            st.subheader(":red[Since eggs are high in protein, hence they are difficult to digest. Thus patients should stay away from eating eggs.]")
            st.write("##")
            st.subheader(":green[In such conditions it is advised to eat food which is easily digestible mostly liquid food and fibre rich food.")
        elif rs == "Abnormal Blood Pressure" :
            st.subheader(":green[Egg consumption has no significant effects on systolic and diastolic blood pressure in adults so it is safe to consume eggs.]")
            st.write("##")
        else :
            st.subheader(":orange[Yes you may,You haven't selected any one of the Categories ]")
    elif res == "Fruits":
        if rs == "Diabetes":
            st.subheader (":green[The National Institute of Diabetes and Digestive and Kidney Diseases recommend that people with diabetes include fruits as part of a balanced diet. Eating fruits and vegetables may put a person at lower risk of developing heart disease and cancer. Fruit is also an important source of vitamins, minerals, and fiber.]")
            st.write("##")
        elif rs == "PCOD":
            st.subheader(":green[Yes,Your PCOD Diet Plan should definitely include fruits daily. You may add fruits like red grapes, cherries, blueberries, blackberries, strawberries and apples to your diet. These fruits are low in glycaemic index (GI), helpful for insulin sensitivity.]")
            st.write("##")
        elif rs =="Dengue" or rs == "Jaundice" :
            st.subheader(":green[Yes , eat a variety of fruits and vegetables every day. Look for high fiber foods, such as oatmeal, broccoli, chickpeas, berries, and almonds.]")
            st.write("##")
        elif rs == "Abnormal Blood Pressure" :
            st.subheader(":green[Yes, you can eat these foods in moderation if you choose to, but check with your doctor first. Just take care to eat about the same amount on a day-to-day basis.]")
            st.write("##")
            st.subheader(":orange[Try not to consume fruits that contain Vitamin K as it acts as a blood thinner ")
        elif rs == "":
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)" or ras == "Underweight(less than 18.5)" or ras == "Normal(18.5 to 25)":
                st.subheader(":[You can have the food item]")
                st.write("##")
        else :
            st.subheader(":orange[Yes,you may have it")
    elif res == "Milk":
        if rs == "Diabetes":
            st.subheader(":green[Yes, people with diabetes can drink milk. Research shows that people with diabetes can drink milk as it benefits in controlling and reducing type 2 diabetes]")
            st.write("##")
        elif rs == "PCOD":
            st.subheader(":green[Dairy foods are not strictly prohibited for women with PCOS, you can consume milk and products to enjoy their nutritive values but in a limit. ]")
            st.write("##")
            st.subheader(":orange[Excess consumption of dairy which is a carbohydrate can lead to an increase in blood glucose level and also stimulate insulin]")
        elif rs == "Jaundice" or rs =="Dengue":
            st.subheader(":red[ Milk products must be totally avoided if one has such condition as they are high in protien and can be difficult to digest]")
            st.write("##")
            st.subheader(":green[It is more prefferable to have fruits and green leafy vegetables")
        elif rs == "Abnormal Blood Pressure":
            st.subheader(":green[Milk products contain key blood pressure lowering nutrients, including calcium, potassium and magnesium.]")
        else :
            st.subheader("You may have it")
    elif res == "Salt":
        if rs == "Diabetes":
            if ras == "Overweight(25 to 30)" or ras == "Obese(more than 30)":
                st.subheader(":red[Salt has no effect on blood glucose level but eating too much sodium in the form of added salt has been associated with weight gain.]")
                st.write("##")
                st.subheader(":green[Salt consumption is important but it should be limited]")
            else :
                st.subheader(":green[Salt has no effect on blood glucose level]")
        if rs == "PCOD":
            st.subheader(":red[PCOD sufferers should limit their sodium intake to a maximum of 2,300 milligrams per day, or -- to be cautious -- 1,500 milligrams daily.]")
            st.write("##")
            st.subheader(":green[Try using pink salt/rock salt as it is not produced by artificial methods")
        if rs == "Jaundice" or rs =="Dengue":
            st.subheader(":red[We recommend choosing low sodium foods or following a low sodium eating plan during such conditions as sodium in foods can cause your body to keep fluids around longer than typical. It could make it harder for your liver to function effectively if you consume too much sodium.]")
            st.write("##")
            st.subheader(":green[Low sodium diet should be preffered]")
        if rs == "Abnormal Blood Pressure":
            st.subheader(":red[Salt consumption should be absolutely minimized in cases of high blood pressure]")
        else :
            st.subheader(":orange[You can consume it]")
    elif res == "Wheat":
        if rs == "Diabetes":
            st.subheader(":green[Yes, whole wheat chapati is best for diabetic as it controls blood sugar spikes and curbs your appetite.]")
        elif rs == "PCOD":
            st.subheader(":green[ Yes, Food made from whole wheat, wheat flour and whole grain can be consumed as they have low glycemic index ]")
        elif rs == "Jaundice" or rs == "Dengue" :
            st.subheader(":green[Wheat can be consumed in such conditions ]")
            st.write("##")
            st.subheader(":orange[Oats is more prefferable as it is a great source of energy and fiber]")
        elif rs == "Abnormal Blood Pressure":
            st.subheader(":green[Yes ,  including fibre in your diet can have a positive effect on people with high blood pressure.")
        else :
            st.subheader("You can have it")
    elif res == "Fish":
        if rs == "Diabetes":
            st.subheader(":green[Yes,fish is a good food for people with diabetes. Protein provides some of our energy needs and omega 3 may help our heart health.]")
        elif rs == "PCOD":
            st.subheader(":green[Yes,fatty fish like salmon and mackerel are rich in omega-3 fatty acids. Since these are considered anti-inflammatory, they are especially good as part of a diet to battle PCOS.")
        elif rs == "Jaundice" or rs =="Dengue":
            st.subheader(":red[No,Rich meats, such as beef and pork, contain high levels of animal amino acids and fats that can be difficult to digest and put a strain on a damaged liver.]")
            st.write("##")
            st.subheader(":green[It is better to have lean meats, such as poultry and fish, as well as plant-based proteins, such as legumes and tofu, are more liver-friendly protein sources.]")
        elif rs == "Abnormal Blood Pressure":
            st.subheader(":green[Yes,they are found to be rich in an important type of polyunsaturated fat called omega-3, which has been shown to help lower blood pressure]")
        else :
            st.subheader(":orange[You can consume the food]")
    elif res == "Chicken/Meat" :
        if rs == "Diabetes":
            st.subheader(":green[Chicken can be a great option for people with diabetes. All cuts of chicken are high in protein and many are low in fat. When prepared in a healthy way, chicken can be a great ingredient in a healthy diabetic eating plan.]")
        elif rs == "PCOD" :
            st.subheader(":green[Lean protein sources like tofu, chicken, and fish don't provide fiber but are a very filling and nutritious dietary option for people with PCOS.]")
        elif rs == "Jaundice" or rs == "Dengue":
            st.subheader(":green[Yes. You can eat but it should be in stew form or in boiled form or less spicy. ]")
        elif rs == "Abnormal Blood Pressure":
            st.subheader(":green[Chicken is one of the best food items you can eat if you have blood pressure.The most important reason why you can add chicken to your diet is that it is high in protein content. Protein, in general, is essential for your body.] ")
        else :
            st.subheader("You can have it")
    elif res == "Cottage Cheese":
        if rs == "Diabetes":
            st.subheader(":green[Cottage cheese is a great snack for people with diabetes. A half-cup (about 112-gram) serving of small-curd cottage cheese provides several vitamins and minerals, in addition to almost 13 grams of protein and only 4 grams of carbs.]")
        elif rs == "PCOD":
            st.subheader(":green[Yes,cottage cheese is a good option as it a source protien")
        elif rs == "Jaundice" or rs == "Dengue":
            st.subheader(":green[Yes, cottage cheese is an easily digestible source of protein. It can be consumed during these conditions.]")
        elif rs == "Abnormal Blood Pressure":
            st.subheader(":green[Cottage cheese can be part of a heart-healthy diet, as it's low in sodium and provides essential nutrients like calcium and protein.]")
        else:
            st.subheader("You can have it")