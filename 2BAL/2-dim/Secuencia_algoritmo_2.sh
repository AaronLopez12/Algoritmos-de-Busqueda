rm *.txt

for i in {1..40}
do
	
	sed 's/iter/'$i'/g'  Actividad2_Blind_Search.py > tmp.py
	python3 tmp.py
	rm tmp.py
done

python3 Analisis_algoritmo_2.py
