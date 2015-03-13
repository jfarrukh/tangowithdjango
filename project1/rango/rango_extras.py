__author__ = '1108297f'

def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}
