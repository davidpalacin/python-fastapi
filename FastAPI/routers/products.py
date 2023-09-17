from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message": "Not found"}})

products_list = ["Poducto 1", "Poducto 2", "Poducto 3", "Poducto 4", "Poducto 5"]

@router.get("/")
async def products():
  return products_list


@router.get("/{id}")
async def product(id: int):
  return products_list[id]