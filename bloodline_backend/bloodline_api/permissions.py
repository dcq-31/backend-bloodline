from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  """
  Custom permission to only allow owners of an dog to edit it.
  """

  def has_object_permission(self, request, view, dog):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    print('CHECKS PERMISION')
    print(request.user)
    print(dog.owner)
    if request.method in permissions.SAFE_METHODS:
        return True

    # Write permissions are only allowed to the owner of the dog.
    return dog.owner == request.user