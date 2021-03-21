# django-extra-fields-on-many-to-many-relationships

When you’re only dealing with many-to-many relationships such as mixing and matching pizzas and toppings, a standard ManyToManyField is all you need. However, sometimes you may need to associate data with the relationship between two models.

For example, consider the case of an application tracking the musical groups which musicians belong to. There is a many-to-many relationship between a person and the groups of which they are a member, so you could use a ManyToManyField to represent this relationship. However, there is a lot of detail about the membership that you might want to collect, such as the date at which the person joined the group.

For these situations, Django allows you to specify the model that will be used to govern the many-to-many relationship. You can then put extra fields on the intermediate model. The intermediate model is associated with the ManyToManyField using the through argument to point to the model that will act as an intermediary.

So, you just have to set up your ManyToManyField to use your intermediary model
