import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

class AsmaraTlahTerKalibrasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas UTS Pegolahan Citra")

        # buat frame untuk menampilkan gambar asli dan hasil citra
        self.image_frame = Frame(self.root)
        self.image_frame.pack(side=TOP)

        # buat canvas untuk menampilkan gambar asli
        self.original_canvas1 = Canvas(self.image_frame, width=300, height=300)
        self.original_canvas1.pack(side=LEFT, padx=10, pady=10)

        self.original_canvas2 = Canvas(self.image_frame, width=300, height=300)
        self.original_canvas2.pack(side=RIGHT, padx=10, pady=10)

        # buat canvas untuk menampilkan hasil citra
        self.processed_canvas = Canvas(self.image_frame, width=300, height=300)
        self.processed_canvas.pack(side=BOTTOM, padx=10, pady=10)

        # buat tombol untuk membuka citra
        open_button = Button(self.root, text="Masukan Gambar Pertama", command=self.open_image1)
        open_button.pack(pady=10)

        open_button = Button(self.root, text="Masukan Gambar KeDua", command=self.open_image2)
        open_button.pack(pady=10)

        # buat tombol untuk melakukan substraksi citra
        substraksi = Button(self.root, text="Gambar Substraksi", command=self.image_subtraction)
        substraksi.pack(pady=10)

        # buat tombol untuk melakukan deteksi tepi citra
        Deteksi_Tepi = Button(self.root, text="Deteksi Tepi", command=self.image_edge_detection)
        Deteksi_Tepi.pack(pady=10)

        # buat tombol untuk melakukan filter pengolahan citra digital
        Filter = Button(self.root, text="Filter", command=self.image_filter)
        Filter.pack(pady=10)

        # buat tombol untuk mengeluarkan nama kelompok
        kelompok = Button(self.root, text="Nama Kelompok", command=self.kelompok)
        kelompok.pack(pady=10)

    # fungsi untuk membuka file citra dan menampilkan gambar asli pada canvas
    def open_image1(self):
        self.filename1 = filedialog.askopenfilename(title="Select file", filetypes=[("Format", "*.jpg;*.jpeg;*.png;*.bmp")])
        image1 = cv2.imread(self.filename1)
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        self.original_image1 = Image.fromarray(image1)
        self.original_image1 = ImageTk.PhotoImage(self.original_image1)
        self.original_canvas1.create_image(0, 0, anchor=NW, image=self.original_image1)

    def open_image2(self):
        self.filename2 = filedialog.askopenfilename(title="Select file", filetypes=[("Format", "*.jpg;*.jpeg;*.png;*.bmp")])
        image2 = cv2.imread(self.filename2)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        self.original_image2 = Image.fromarray(image2)
        self.original_image2 = ImageTk.PhotoImage(self.original_image2)
        self.original_canvas2.create_image(0, 0, anchor=NW, image=self.original_image2)

    # fungsi untuk menampilkan hasil citra pada canvas
    def show_processed_image(self, processed_image):
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        self.processed_image = Image.fromarray(processed_image)
        self.processed_image = ImageTk.PhotoImage(self.processed_image)
        self.processed_canvas.create_image(0, 0, anchor=NW, image=self.processed_image)

    # fungsi untuk melakukan substraksi citra dan menampilkan hasil citra pada canvas
    def image_subtraction(self):
        image1 = cv2.imread(self.filename1)
        image2 = cv2.imread(self.filename2)
        # konversi citra ke grayscale
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        # lakukan substraksi citra
        subtracted_image = cv2.subtract(gray1, gray2)
        # tampilkan citra hasil substraksi pada canvas
        self.show_processed_image(subtracted_image)

    # fungsi untuk melakukan deteksi tepi citra dan menampilkan hasil citra pada canvas
    def image_edge_detection(self):
        image = cv2.imread(self.filename1)
        # konversi citra ke grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # lakukan deteksi tepi dengan metode Canny
        edges = cv2.Canny(gray, 100, 200)
        # tampilkan citra hasil deteksi tepi pada canvas
        self.show_processed_image(edges)

    # fungsi untuk melakukan filter pengolahan citra digital dan menampilkan hasil citra pada canvas
    def image_filter(self):
        image = cv2.imread(self.filename1)
        # lakukan filter pengolahan citra digital dengan kernel Gaussian Blur
        filtered_image = cv2.GaussianBlur(image, (5,5), 0)
        # tampilkan citra hasil filter pada canvas
        self.show_processed_image(filtered_image)

    def kelompok(self):
        kelompok = tk.Tk()
        kelompok.title("Kelompok UTS")
        kelompok.geometry("300x300")
        frm=ttk.Frame(kelompok,relief="groove")
        frm.place(x=25,y=25,width=250,height=250)
        self.anggota1=ttk.Label(frm,text="Azri Aulia Choiru Akmal (K1C020037)")
        self.anggota1.place(x= 1,y=20)
        self.anggota2=ttk.Label(frm,text="Rafi Satria Dwi Awanda (K1C021065)")
        self.anggota2.place(x= 1,y=40)
        self.anggota3=ttk.Label(frm,text="Zakiyah Nurseha (K1C021073)")
        self.anggota3.place(x= 1,y=60)

# buat objek ImageProcessor dan jendela utama Tkinter
root = Tk()
app = AsmaraTlahTerKalibrasi(root)
root.mainloop()