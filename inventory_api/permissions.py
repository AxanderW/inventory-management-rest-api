from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def  has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id



class AccessUpdateInventory(permissions.BasePermission):
    """Allow staff to get and modify inventory"""
    def  has_object_permission(self, request, view, obj):
        """ User is staff"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff == True


## TODO: create permission that allows authenticated users to get data read_only
## BUT restricts post and update methods to user where is_staff == True
"""
    Permissions class only for manipulating products, regions, brands, and orders

            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.is_staff == True

"""
