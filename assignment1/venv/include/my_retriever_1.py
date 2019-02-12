import numpy as np

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting

        doc_all = []
        for term in index:
            doc_all.extend(index[term])
        self.Doc = len(set(list(doc_all)))




    def forQuery(self, query):

        #declare some array and dictionary
        id_relevant = []
        value_query = {}
        value_index = {}
        D = self.Doc
        element = {}

        for term in query:
            if term in self.index:
                id_relevant.extend(self.index[term].keys())
        id_relevant = np.unique(id_relevant)
        # print(term)
        # print(re)
        for term in self.index:
            idf = np.log10(D / len(self.index[term].keys()))
            if term in query:
                if self.termWeighting == "tf":
                    value_query[term] = query[term]
                if self.termWeighting == "binary":
                    value_query[term] = 1
                if self.termWeighting == "tfidf":
                    value_query[term] = query[term] * idf


            for id in self.index[term]:
                if id in id_relevant:
                    if id not in value_index:
                        value_index[id] = {}
                    if self.termWeighting == "tfidf":
                        value_index[id][term] = self.index[term][id] * idf
                    if self.termWeighting == "tf":
                        value_index[id][term] = self.index[term][id]
                    if self.termWeighting == "binary":
                        value_index[id][term] = 1 if id in self.index[term] else 0
                    if id not in element:
                        element[id] = 0
                    if term in query:
                        element[id] += value_index[id][term]*value_query[term]

        index = self.calculate_similarity(value_index, value_query, element)
        return index


    def calculate_similarity(self, value_index, value_query, element):
        simi = {}
        value_query_one = np.asarray(list(value_query.values()))
        for id in value_index:
            value_index_one = np.asarray(list(value_index[id].values()))
            denominator = np.sqrt((value_index_one**2).sum()) * np.sqrt((value_query_one**2).sum())
            if denominator == 0 :
                simi[id] = 0
            else:
                simi[id] = element[id] / denominator

        index = np.argsort(list(simi.values()))

        return np.array(list(simi.keys()))[index[-10:]]









