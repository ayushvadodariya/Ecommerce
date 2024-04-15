import React, { useState } from 'react';
import axios from 'axios';

function AddProduct() {
    const [productName, setProductName] = useState('');
    const [productImages, setProductImages] = useState([]);
    const [error, setError] = useState('');

    const handleFileChange = (e) => {
        setProductImages(e.target.files);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(`${productImages.toString}`);

        try {
            const formData = new FormData();
            formData.append('productName', productName);
            for (let i = 0; i < productImages.length; i++) {
                formData.append('productImages', productImages[i]);
            }

            const response = await axios.post('/api/v1/product/add', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            console.log(response.data);
            // Handle success
        } catch (error) {
            console.error(error);
            setError('An error occurred while adding the product.');
        }
    };

    return (
        <div>
            <h2>Add Product</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="productName">Product Name:</label>
                    <input
                        type="text"
                        id="productName"
                        value={productName}
                        onChange={(e) => setProductName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="productImages">Product Images:</label>
                    <input
                        type="file"
                        id="productImages"
                        multiple
                        onChange={handleFileChange}
                    />
                </div>
                <button type="submit">Add Product</button>
                {error && <p style={{ color: 'red' }}>{error}</p>}
            </form>
        </div>
    );
}

export default AddProduct;