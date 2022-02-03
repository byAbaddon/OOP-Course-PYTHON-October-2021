class Storage:
    categories, topics, documents = [], [], []  
    
    def add_category(self, category): # add the category if it does not exist
        if category not in self.categories:
            self.categories.append(category)


    def add_topic(self, topic): # add the topic if it does not exist
        if topic not in self.topics:
            self.topics.append(topic)


    def add_document(self, document): #add the document if it does not exist
        if document not in self.documents:
            self.documents.append(document)
        
    def edit_category(self, category_id , new_name): # edit the name of the category with the provided id
        find_category = [x for x in self.categories if x.id == category_id][0]
        if find_category:
            find_category.edit(new_name)
            

    def edit_topic(self, topic_id , new_topic, new_storage_folder): # edit the topic with the given id
        find_topic = [x for x in self.topics if x.id == topic_id][0]
        if find_topic:
            find_topic.edit(new_topic, new_storage_folder)


    def edit_document(self, document_id, new_file_name): # edit the document with the given id
        find_document = [x for x in self.documents if x.id == document_id][0]
        if find_document:
            find_document.edit(new_file_name)

    def delete_category(self, category_id): # delete the category with the provided id
        del_category = [x for x in self.categories if x.id == category_id][0]
        if del_category:
            self.categories.remove(del_category)    


    def delete_topic(self, topic_id): # – delete the topic with the provided id
        del_topic = [x for x in self.topics if x.id == topic_id][0]
        if del_topic:
            self.topics.remove(del_topic)  


    def delete_document(self, document_id): # delete the document with the provided id
        del_document = [x for x in self.documents if x.id == document_id][0]
        if del_document:
            self.documents.remove(del_document)


    def get_document(self, document_id): # return the document with the provided id
        return_document = [x for x in self.documents if x.id == document_id][0]
        if return_document:
            return return_document

    def __repr__(self): # returns a string representation of each document on separate lines
        result = ''
        for el in self.documents:
            result += f'{el}\n'
        return result

