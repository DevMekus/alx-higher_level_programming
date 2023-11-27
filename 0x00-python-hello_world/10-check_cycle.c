#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
        listint_t *slowmove = list;
        listint_t *fastmove = list;

        if (!list)
                return (0);

        while (slowmove && fastmove && fastmove->next)
        {
                slowmove = slowmove->next;
                fastmove = fastmove->next->next;
                if (slowmove == fastmove)
                        return (1);
        }

        return (0);
}
