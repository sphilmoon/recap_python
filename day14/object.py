# day 14, object-oriented programmaing (OOP)
# classes and objects 

class RNASample: 
    def __init__(self, sample_id, quality):
        self.sample_id = sample_id
        self.quality = quality 

    def display_info(self):
        print(f"ID: {self.sample_id}, Quality {self.quality}%")
              
    def update_quality(self, new_quality):
        self.quality = new_quality
        print(f"Quality for {self.sample_id} is updated to {self.quality}%")


# creating an instance (object), then call the method. 
sample1 = RNASample("Sample_001", 94.5)
sample1.display_info() 
sample1.update_quality(98.1)
sample1.display_info() 

#print(sample1.sample_id)
#print(sample1.quality)