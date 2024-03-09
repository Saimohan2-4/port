# Create a file with all the states and their postal codes
echo "Alabama,AL\nAlaska,AK\nArizona,AZ\nArkansas,AR\nCalifornia,CA\nColorado,CO\nConnecticut,CT\nDelaware,DE\nFlorida,FL\nGeorgia,GA\nHawaii,HI\nIdaho,ID\nIllinois,IL\nIndiana,IN\nIowa,IA\nKansas,KS\nKentucky,KY\nLouisiana,LA\nMaine,ME\nMaryland,MD\nMassachusetts,MA\nMichigan,MI\nMinnesota,MN\nMississippi,MS\nMissouri,MO\nMontana,MT\nNebraska,NE\nNevada,NV\nNew Hampshire,NH\nNew Jersey,NJ\nNew Mexico,NM\nNew York,NY\nNorth Carolina,NC\nNorth Dakota,ND\nOhio,OH\nOklahoma,OK\nOregon,OR\nPennsylvania,PA\nRhode Island,RI\nSouth Carolina,SC\nSouth Dakota,SD\nTennessee,TN\nTexas,TX\nUtah,UT\nVermont,VT\nVirginia,VA\nWashington,WA\nWest Virginia,WV\nWisconsin,WI\nWyoming,WY" > states_and_codes.txt

# Randomly shuffle the lines
shuf states_and_codes.txt > randomized_states_and_codes.txt

# Duplicate the lines to create a file with 17092 rows
yes "$(cat randomized_states_and_codes.txt)" | head -n 17092 > states_and_codes.csv

# Clean up temporary files
rm states_and_codes.txt randomized_states_and_codes.txt

