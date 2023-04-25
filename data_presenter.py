import pandas as pd
# import matplotlib.pyplot as plt

class DataPresenter:
    def generate_axis_data(self, projects):
        df = self.scalars_to_df(projects)
        
        x = df.tag.groupby(df.tag).count().index
        y = df.tag.groupby(df.tag).count()
        # list of squares
        return  [x, y]
    
        
        
    def scalars_to_df(self, scalars_projects):
        list_projects = []
        for p_obj in scalars_projects:
            for tag in p_obj.tags:
                if tag.name == '':
                    continue
                project = []
                project.append(tag.name)
                project.append(p_obj.title)
                project.append(p_obj.url)
                project.append(p_obj.description)
                project.append(p_obj.posted_date)
                project.append(p_obj.deadline)
                project.append(p_obj.expected_time_limit)
                project.append(p_obj.price_fixed)
                project.append(p_obj.price_fixed_min)
                project.append(p_obj.price_hourly)
                project.append(p_obj.price_hourly_min)

                list_projects.append(project)

        return pd.DataFrame(list_projects ,columns=["tag","title","url","description","posted_date","deadline","expected_time_limit",\
                                "price_fixed","price_fixed_min","price_hourly","price_hourly_min"])
