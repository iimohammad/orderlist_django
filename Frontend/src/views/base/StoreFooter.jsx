import React from 'react';

function StoreFooter() {
    return (
        <footer className="bg-dark text-light py-4">
            <div className="container">
                <div className="row">
                    <div className="col-md-4 mb-4">
                        <h5>Navigation</h5>
                        <ul className="list-unstyled">
                            <li><a href="/">Home</a></li>
                            <li><a href="/products">Products</a></li>
                            <li><a href="/about">About Us</a></li>
                            <li><a href="/contact">Contact Us</a></li>
                        </ul>
                    </div>
                    <div className="col-md-4 mb-4">
                        <h5>Contact Us</h5>
                        <address>
                            123 Store St<br />
                            City, State 12345<br />
                            Phone: (123) 456-7890<br />
                            Email: info@store.com
                        </address>
                    </div>
                    <div className="col-md-4 mb-4">
                        <h5>Connect With Us</h5>
                        <ul className="list-inline social-icons">
                            <li className="list-inline-item"><a href="#"><i className="bi bi-facebook"></i></a></li>
                            <li className="list-inline-item"><a href="#"><i className="bi bi-twitter"></i></a></li>
                            <li className="list-inline-item"><a href="#"><i className="bi bi-instagram"></i></a></li>
                            <li className="list-inline-item"><a href="#"><i className="bi bi-linkedin"></i></a></li>
                        </ul>
                    </div>
                </div>
                <div className="row">
                    <div className="col text-center">
                        <p>&copy; 2024 Your Store. All rights reserved.</p>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default StoreFooter;
