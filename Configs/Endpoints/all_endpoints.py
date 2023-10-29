PRICES = {

    # Excel
    "download_file": "api/prices/api/v1/file",  # GET (TODO)
    "upload_file": "api/prices/api/v1/file",  # POST

    # Prices
    "get_prices": "api/prices/api/v1/tasks/{task_id}/prices",  # POST
    "get_filter_def": "api/prices/api/v1/prices/_filterdef",  # GET
    "delete_prices": "api/prices/api/v1/prices/batchDelete",  # DELETE (TODO)
    "get_product_categories": "api/prices/api/v1/prices/categories",  # GET (TODO)
    "get_category_with_products": "api/prices/api/v1/prices/products",  # POST (TODO)
    "get_price_details": "api/prices/api/v1/prices/{price_id}/details",  # GET (TODO)
    "get_price_stages": "api/prices/api/v1/prices/{price_id}/stages",  # POST (TODO)
    "get_task_prices": "api/prices/api/v1/prices/{task_id}/prices",  # POST (TODO)
    "send_prices_to_1c": "api/prices/api/v1/prices/{task_id}/prices/send",  # POST (TODO)

    # Rules
    "get_rules": "api/prices/api/v1/prices/rules",  # GET
    "create_rule": "api/prices/api/v1/prices/rules",  # POST
    "get_filter_def_rules": "api/prices/api/v1/prices/rules/_filterdef",  # GET
    "run_rule": "api/prices/api/v1/prices/rules/{rule_id}/run",  # POST (TODO)
    "commit_rule": "api/prices/api/v1/prices/rules/{rule_id}/scenario/commit",  # POST (not working)
    "start_rule": "api/prices/api/v1/prices/rules/{rule_id}/start",  # POST (TODO)
    "stop_rule": "api/prices/api/v1/prices/rules/{rule_id}/stop",  # POST (TODO)
    "get_rule": "api/prices/api/v1/prices/rules/{rule_id}",  # GET
    "edit_rule": "api/prices/api/v1/prices/rules/{rule_id}",  # PUT
    "delete_rule": "api/prices/api/v1/prices/rules/{rule_id}",  # DELETE
    "copy_rule": "api/prices/api/v1/prices/rules/{rule_id}/create_copy",  # POST
    "get_products": "api/prices/api/v1/prices/rules/{rule_id}/products",  # GET (TODO)
    "upload_products": "api/prices/api/v1/prices/rules/{rule_id}/products/file",  # POST (TODO)
    "get_operations": "api/prices/api/v1/prices/operations",  # GET (TODO)
    "get_rule_operations": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations",  # GET
    "get_rule_operation": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations/{operation_id}",  # GET
    "get_shops": "api/prices/api/v1/prices/rules/{rule_id}/shops",  # POST (TODO)
    "upload_shops": "api/prices/api/v1/prices/rules/{rule_id}/shops/file",  # POST (TODO)

    # Edit Rule
    "save_price_list": "api/prices/api/v1/prices/rules/{rule_id}/price_list",  # POST
    "save_price_period": "api/prices/api/v1/prices/rules/{rule_id}/price_period",  # POST
    "save_repetition_schedule": "api/prices/api/v1/prices/rules/{rule_id}/repetition_schedule",  # POST (TODO)
    "add_operation": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations",  # POST
    "edit_operation": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations/{operation_id}",  # PUT
    "delete_operation": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations/{operation_id}",  # DELETE
    "get_delete_info": "api/prices/api/v1/prices/rules/{rule_id}/scenario/operations/{operation_id}/_deleteinfo",  # GET (TODO)

    # shelf_price
    "get_shelf_prices_regions": "api/prices/api/v1/prices/shelf/{product_code}/regions",  # POST (TODO)

    # tasks
    "get_tasks": "api/prices/api/v1/tasks",  # POST
    "delete_task": "api/prices/api/v1/tasks/{task_id}",  # GET
    "get_task_by_id": "api/prices/api/v1/tasks/{task_id}",  # GET (TODO)
    "delete_tasks": "api/prices/api/v1/tasks",  # DELETE (TODO)
    "get_rule_by_task": "api/prices/api/v1/tasks/{task_id}/rule",  # GET (TODO)

    # templates
    "get_tasks_template": "api/prices/api/v1/tasks_template",  # GET (TODO)
    "create_tasks_template": "api/prices/api/v1/tasks_template",  # PUT (TODO)
    "get_task_template": "api/prices/api/v1/tasks_template/{id}",  # GET (TODO)
    "update_task_template": "api/prices/api/v1/tasks_template/{id}",  # PUT (TODO)
    "delete_task_template": "api/prices/api/v1/tasks_template/{id}",  # DELETE (TODO)

}