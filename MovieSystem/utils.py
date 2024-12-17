class PaginatorMixin:
    def get_page(self, paginator, page, page_offset=2):
        left_more_page = False
        right_more_page = False
        # 获取当前页码
        # 如果当前页面是7
        current_num = page.number
        if current_num <= page_offset + 2:
            left_range = range(1, current_num)
        else:
            left_more_page = True
            left_range = range(current_num - page_offset, current_num)
        if current_num >= paginator.num_pages - page_offset - 1:
            right_range = range(current_num + 1, paginator.num_pages + 1)
        else:
            right_more_page = True
            right_range = range(current_num + 1, current_num + page_offset + 1)
        return {
            'left_range': left_range,
            'right_range': right_range,
            'left_more_page': left_more_page,
            'right_more_page': right_more_page,
        }