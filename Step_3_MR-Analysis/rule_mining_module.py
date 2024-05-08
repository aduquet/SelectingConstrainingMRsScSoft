from mlxtend.frequent_patterns import apriori, association_rules
from itertools import combinations
import pandas as pd

class RuleMiningModule(object):
    
    def __init__(self, data, support, conf):
        self.data = data
        self.support = support
        self.conf = conf

    def enconde(self):
        
        df = self.data.copy()
        df = df.drop(columns = ['key_original_file', 'vs', 'contains_floats', 'contains_integers'])

        for col in df.columns:
            df[col] = df[col].astype(str)

        # Apply one-hot encoding to convert categorical data to binary format
        df_encoded = pd.get_dummies(df)
        
        return df_encoded
    
    def ruleGenerator_v(self, df_encode, path_store):
        df_encode = df_encode.drop(columns = ['vs_str_No-violate'])

        # Apply the Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori(df_encode, min_support=0.1, use_colnames=True)

        # Generate association rules
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

        # Filter rules where 'vs_str_Violate' is the only item in the consequents
        violated_rules = rules[
            (rules['consequents'].astype(str).str.contains("'vs_str_Violate'")) & 
            (rules['consequents'].apply(lambda x: len(x) == 1))]       
        # Filter rules with lift greater than 1
        relevant_rules = violated_rules[violated_rules['lift'] > 1]

        relevant_rules['antecedents'] = relevant_rules['antecedents'].apply(lambda x: list(x))
        relevant_rules['consequents'] = relevant_rules['consequents'].apply(lambda x: list(x))
        
        rs = relevant_rules.sort_values(by='antecedent support', ascending=False)
        rs.to_csv( path_store + '_v.csv', index=False)

        contradictory_antecedents = [
            ['weigth_of_list_wn', 'has_zeros_False'],
            ['weigth_of_list_wn', 'has_zeros_True'],
            ['weigth_of_list_wn', 'has_duplicates_False'],
            ['weigth_of_list_wn', 'has_duplicates_True'],
            ['weigth_of_list_wn', 'is_sorted_False'],
            ['weigth_of_list_wn', 'is_sorted_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_True'],
            ['weigth_of_list_wn', 'contains_even_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_False'],
            ['weigth_of_list_wn', 'contains_odd_numbers_True'],
            ['weigth_of_list_wn', 'more_positive_or_negative_e'],
            ['weigth_of_list_wn', 'more_positive_or_negative_n'],
            # Add more contradictory antecedents as needed
        ]
        # filter_rules = relevant_rules[~relevant_rules['antecedents'].apply(lambda x: any(set(contradiction).issubset(x) for contradiction in contradictory_antecedents))]

        # filter_rules.to_csv( path_store + '_filtered_v.csv', index=False)

    def ruleGenerator_nv(self, df_encode, path_store):
            df_encode = df_encode.drop(columns = ['vs_str_Violate'])

            # Apply the Apriori algorithm to find frequent itemsets
            frequent_itemsets = apriori(df_encode, min_support=0.1, use_colnames=True)

            # Generate association rules
            rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

            # Filter rules where 'vs_str_Violate' is the only item in the consequents
            violated_rules = rules[
                (rules['consequents'].astype(str).str.contains("'vs_str_No-violate'")) & 
                (rules['consequents'].apply(lambda x: len(x) == 1))]       
            # Filter rules with lift greater than 1
            relevant_rules = violated_rules[violated_rules['lift'] > 1]

            relevant_rules['antecedents'] = relevant_rules['antecedents'].apply(lambda x: list(x))
            relevant_rules['consequents'] = relevant_rules['consequents'].apply(lambda x: list(x))
            
            rs = relevant_rules.sort_values(by='antecedent support', ascending=False)
            rs.to_csv( path_store + '_nv.csv', index=False)

            contradictory_antecedents = [
                ['weigth_of_list_wn', 'has_zeros_False'],
                ['weigth_of_list_wn', 'has_zeros_True'],
                ['weigth_of_list_wn', 'has_duplicates_False'],
                ['weigth_of_list_wn', 'has_duplicates_True'],
                ['weigth_of_list_wn', 'is_sorted_False'],
                ['weigth_of_list_wn', 'is_sorted_True'],
                ['weigth_of_list_wn', 'contains_even_numbers_True'],
                ['weigth_of_list_wn', 'contains_even_numbers_False'],
                ['weigth_of_list_wn', 'contains_odd_numbers_False'],
                ['weigth_of_list_wn', 'contains_odd_numbers_True'],
                ['weigth_of_list_wn', 'more_positive_or_negative_e'],
                ['weigth_of_list_wn', 'more_positive_or_negative_n'],
                # Add more contradictory antecedents as needed
            ]
            # filter_rules = relevant_rules[~relevant_rules['antecedents'].apply(lambda x: any(set(contradiction).issubset(x) for contradiction in contradictory_antecedents))]

            # filter_rules.to_csv( path_store + '_filtered_nv.csv', index=False)


    def generate_or_rules(seld, rules):
        new_rules = []
        for _, rule in rules.iterrows():
            antecedents = rule['antecedents']
            if 'vs_str_Violate' in rule['consequents']:
                consequents = ['vs_str_Violate']
                for antecedent_comb in combinations(antecedents, 2):
                    new_rule = tuple(antecedent_comb) + tuple(consequents)
                    new_rules.append({'antecedents': set(antecedent_comb), 'consequents': consequents})
        return pd.DataFrame(new_rules)

        # Generate rules with 'or' conditions


        # df_encode = pd.get_dummies(df_encode)
        # print(df_encode)
        # itemSets, rules = apriori(df_encode, min_support=self.support)
        
        # rules = association_rules(itemSets, metric="confidence", min_threshold=0.7)

        # # Filter rules where 'vs_str' is violated
        # violated_rules = rules[rules['consequents'].astype(str).str.contains("'vs_str_Violate'")]

        # print(violated_rules)

        # return itemSets, rules