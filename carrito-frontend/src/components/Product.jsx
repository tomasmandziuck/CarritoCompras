import React , {useContext} from "react"
import { CartContext } from "./context/CartContext";


export const Product = ({ name, price, id, imgUrl }) => {
    const [cart, setCart] = useContext(CartContext)

    const addToCart = () =>{
        setCart((currentProducts)=>{
            const isInCart = currentProducts.find((product)=> product.id === id);
            if(isInCart){
                return currentProducts.map((product)=>{
                    if (product.id === id){
                        return {...product, quantity: product.quantity +1};
                    }else {
                        return product;
                    }
                });
            }else {
                return [...currentProducts, {id, quantity : 1, price}];
            }

        });
    };


    const removeProduct = () =>{
        setCart((currentProducts)=>{
            if (currentProducts.find((product)=> product.id === id)?.quantity === 1){
                return currentProducts.filter((product) => product.id !== id);
            }else {
                return currentProducts.map((product)=>{
                    if (product.id === id){
                        return {...product, quantity:product.quantity -1};
                    }else {
                        return product
                    }
                });
            }
        });
    };

    const getQuantityById = (id) => {
        return cart.find((item) => item.id === id)?.quantity || 0;
    };

    const itemQuantity = getQuantityById(id);

  return (
    <div className="product-box">
        {
           itemQuantity > 0 && (
            <div className="product-quantity">{itemQuantity}</div>
           )
        }
      <div>{name}</div>
      <img src={imgUrl} width="80" height="55" />
      <div className="product-price">${price}</div>
      <button className="product-add-button" onClick={()=> addToCart()}>+add to cart</button>

      {
        itemQuantity > 0 && (
            <button className="product-minus-button" onClick={()=> removeProduct()}>+remove item</button>
           )
      }
    </div>
  );
};