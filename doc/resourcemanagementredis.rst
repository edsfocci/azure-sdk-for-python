Redis Cache Management
======================

For general information on resource management, see :doc:`Resource Management<resourcemanagement>`.

Create the management client
----------------------------

The following code creates an instance of the management client.

You will need to provide your ``subscription_id`` which can be retrieved
from `your subscription list <https://manage.windowsazure.com/#Workspaces/AdminTasks/SubscriptionMapping>`__.

See :doc:`Resource Management Authentication <resourcemanagementauthentication>`
for details on getting a ``Credentials`` instance.

.. code:: python

    from azure.mgmt.redis import RedisManagementClient, RedisManagementClientConfiguration

    # TODO: Replace this with your subscription id
    subscription_id = '33333333-3333-3333-3333-333333333333'
    # TODO: See above how to get a Credentials instance
    credentials = ...

    redis_client = RedisManagementClient(
        RedisManagementClientConfiguration(
            credentials,
            subscription_id
        )
    )

Registration
------------

Some operations in the ARM APIs require a one-time registration of the
provider with your subscription.

Use the following code to do the registration. You can use the same
credentials you created in the previous section.

.. code:: python

    from azure.mgmt.resource.resources import ResourceManagementClient, ResourceManagementClientConfiguration

    resource_client = ResourceManagementClient(
        ResourceManagementClient(
            credentials,
            subscription_id
        )
    resource_client.providers.register('Microsoft.Cache')

Create Redis Cache
------------------

The following code creates a new redis cache under an existing resource group.
To create or manage resource groups, see :doc:`Resource Management<resourcemanagement>`.

.. code:: python

    from azure.mgmt.redis.models import Sku, RedisCreateOrUpdateParameters

    group_name = 'myresourcegroup'
    cache_name = 'mycachename'
    redis_cache = redis_client.redis.create_or_update(
        group_name, 
        cache_name,
        RedisCreateOrUpdateParameters( 
            sku = Sku(name = 'Basic', family = 'C', capacity = '1'),
            location = "West US"
        )
    ) 
    # redis_cache is a RedisResourceWithAccessKey instance
